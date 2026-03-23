# Ghi chú về Database (SQLite3)

Tài liệu này tổng hợp các kiến thức cơ bản về SQLite3 và SQL bạn cần ghi nhớ khi phát triển dự án Poker.

## 1. Các kiểu dữ liệu cơ bản trong SQLite
SQLite có 5 kiểu dữ liệu chính (khác một chút so với Python):

| Kiểu dữ liệu SQL | Ý nghĩa | Tương ứng trong Python |
| :--- | :--- | :--- |
| **NULL** | Giá trị rỗng (không có dữ liệu) | `None` |
| **INTEGER** | Số nguyên (1, 2, 3...) | `int` |
| **REAL** | Số thực (3.14, 0.5...) | `float` |
| **TEXT** | Chuỗi văn bản (tên, mật khẩu...) | `str` |
| **BLOB** | Dữ liệu nhị phân (hình ảnh, file...) | `bytes` |

---

## 2. Các câu lệnh SQL quan trọng (CRUD)
CRUD là 4 thao tác cơ bản: Create (Tạo), Read (Đọc), Update (Sửa), Delete (Xóa).

### Tạo bảng (Create Table)
```sql
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    username TEXT UNIQUE NOT NULL,
    balance INTEGER DEFAULT 5000
);
```

### Thêm dữ liệu (Insert)
```sql
INSERT INTO users (username, password, balance) VALUES ('phuc', 'hashed_pass', 5000);
```

### Đọc dữ liệu (Select)
*   **Lấy tất cả:** `SELECT * FROM users;`
*   **Lấy theo điều kiện:** `SELECT * FROM users WHERE username = 'phuc';`

### Cập nhật dữ liệu (Update)
```sql
UPDATE users SET balance = balance - 100 WHERE username = 'phuc';
```

### Xóa dữ liệu (Delete)
```sql
DELETE FROM users WHERE id = 1;
```

---

## 3. Quy trình làm việc với SQLite trong Python
Hãy nhớ quy trình 5 bước này:

1.  **Kết nối (`connect`)**: `con = sqlite3.connect("tên_file.db")`
2.  **Tạo con trỏ (`cursor`)**: `cur = con.cursor()`
3.  **Thực thi lệnh (`execute`)**: `cur.execute("câu_lệnh_sql_ở_đây")`
4.  **Lưu thay đổi (`commit`)**: `con.commit()` (CỰC KỲ QUAN TRỌNG - nếu không sẽ mất dữ liệu).
5.  **Đóng kết nối (`close`)**: `con.close()`

---

## 4. Các lưu ý "Sống còn" cho người mới
*   **Mã hóa mật khẩu**: Đừng bao giờ lưu mật khẩu dưới dạng văn bản thường. Luôn dùng `hashlib` để băm mật khẩu.
*   **SQL Injection**: Tránh dùng chuỗi f-string (ví dụ: `f"SELECT * FROM users WHERE name = '{name}'"`) để truy vấn vì rất dễ bị hack. Hãy dùng dấu chấm hỏi `?` (ví dụ: `cur.execute("... WHERE name = ?", (name,))`).
*   **AUTOINCREMENT**: Khi tạo ID, dùng `AUTOINCREMENT` giúp SQLite tự động tăng số ID cho mỗi người dùng mới, bạn không cần phải tính toán ID tiếp theo là bao nhiêu.
*   **Ghi chú**: SQL không phân biệt chữ hoa chữ thường (`select` giống `SELECT`), nhưng viết HOA các từ khóa (`SELECT`, `FROM`, `WHERE`) sẽ giúp code dễ đọc và chuyên nghiệp hơn.
