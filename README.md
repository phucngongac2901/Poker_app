# poker-app

```bash
# init project
uv init

uv venv

# active venv
.venv\Scripts\activate

uv pip show uvicorn #show version

uv run uvicorn server:app --reload

uvicorn server:app --reload
```








# kiểu lệnh thiết kế nút bấm
self.button_blackjack.setStyleSheet("""
    QPushButton {
        background-color: #2Ecc71; /* Màu nền xanh lá cây */
        color: white;              /* Chữ màu trắng */
        font-size: 16px;           /* Cỡ chữ to ra */
        font-weight: bold;         /* Gạch đậm chữ */
        font-family: Arial;        /* Kiểu chữ */
    }
""")







#(Hover & Pressed)
self.button_blackjack.setStyleSheet("""
    /* 1. TRẠNG THÁI BÌNH THƯỜNG */
    QPushButton {
        background-color: #e74c3c;  /* Màu đỏ */
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
    }
    
    /* 2. KHI CHUỘT LƯỚT QUA (Hover) */
    QPushButton:hover {
        background-color: #c0392b;  /* Màu đổi sang đỏ sậm hơn xíu */
    }
    
    /* 3. KHI BẤM CHUỘT XUỐNG (Pressed) */
    QPushButton:pressed {
        background-color: #a5281b;  /* Đỏ siêu sậm */
        margin-top: 3px;            /* Nút bị lún xuống 3 pixel (Hiệu ứng vật lý 3D) */
    }
""")

