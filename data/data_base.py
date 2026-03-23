import sqlite3
import hashlib

DB_NAME = "account.db"

def init_db():
    """Khoi tao database va tao bảng nếu chưa tồn tại"""
    con = sqlite3.connect(DB_NAME)
    # con: connect to database
    cur = con.cursor()
    # cur: con tro de thuc thi truy van
    # Tao bang voi truong balance (so tien) de game poker co the dung luon
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            balance INTEGER DEFAULT 5000
        )
    """)
    con.commit()
    con.close()

def hash_password(password):
    """Ma hoa mat khau de khong bi lo thong tin duoi dang van ban thuan"""
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    """Dang ky nguoi dung moi"""
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        
        hashed_pw = hash_password(password)
        cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_pw))
        
        con.commit()
        con.close()
        return True, "Đăng ký thành công!"
    except sqlite3.IntegrityError:
        return False, "Tên đăng nhập đã tồn tại!"
    except Exception as e:
        return False, f"Lỗi: {str(e)}"

def login_user(username, password):
    """Kiem tra thong tin dang nhap"""
    con = sqlite3.connect(DB_NAME)
    cur = con.cursor()
    
    hashed_pw = hash_password(password)
    cur.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_pw))
    
    user = cur.fetchone()
    con.close()
    
    if user:
        return True, user # Tra ve thong tin user neu thanh cong
    else:
        return False, None

# Khoi tao database ngay khi file nay duoc chay lan dau
if __name__ == "__main__":
    init_db()
    print("Database da duoc khoi tao!")