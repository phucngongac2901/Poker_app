import sys
# Kéo class BlackJackWindow từ file ui.py sang đây
from file_game.black_jack.ui import BlackJackWindow

from PySide6.QtWidgets import QApplication, QPushButton, QMainWindow, QStackedWidget, QWidget, QVBoxLayout
from PySide6.QtCore import Slot, Qt
from PySide6.QtWidgets import QLabel
from PySide6.QtGui import QPixmap, QBrush, QPalette

class WarningBtn(QPushButton):

    def set_Yellow_color(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #F4FA58; /* Yellow background */
                color: black;              /* black text */
                border: 2px solid #F4FA58; /* Yellow border */
                padding: 10px 20px;        /* Padding around text */
                border-radius: 8px;        /* Rounded corners */
                font-size: 16px;           /* Larger font */
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker green on hover */
            }
            QPushButton:pressed {
                background-color: #388e3c; /* Even darker green when pressed */
            }
        """)

class Mainbtn(QPushButton):

    def set_White_color(self):
        self.setStyleSheet("""
            QPushButton {
                background-color: #FFFFFF; /* White background */
                color: black;              /* black text */
                border: 2px solid #FFFFFF; /* White border */
                padding: 10px 20px;        /* Padding around text */
                border-radius: 8px;        /* Rounded corners */
                font-size: 16px;           /* Larger font */
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker green on hover */
            }
            QPushButton:pressed {
                background-color: #388e3c; /* Even darker green when pressed */
            }
        """)



# cửa sổ bat dau
class PokerGameWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 100, 800, 400) # x, y, width, height

        container = QWidget()
        layout = QVBoxLayout()
        
        # (2) Tải bức tranh từ file lưu trên máy vào bộ nhớ thành QPixmap
        hinh_nen = QPixmap("./file_anh/main_theme.jpg")
        
        # (Lựa chọn) Bóp nắn, kéo dãn tấm hình cho vừa in với size cửa sổ (800x400)
        hinh_nen_vua_khit = hinh_nen.scaled(self.size()) 
        # (3) Tạo một cái bảng màu (Palette), dùng công cụ Lăn Sơn (QBrush) lăn tấm hình đó lên tường
        bang_mau = self.palette()
        bang_mau.setBrush(QPalette.Window, QBrush(hinh_nen_vua_khit))
        # (4) Nộp bản sơn tường đó cho cửa sổ
        self.setPalette(bang_mau)
       
         # Add a back button
        back_button = QPushButton("Quay lai")
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button, alignment = Qt.AlignLeft | Qt.AlignTop)
        
        # Nội dung chính
        
        self.button_blackjack = Mainbtn("Blackjack")
        self.button_blackjack.setFixedSize(200, 50)
        self.button_blackjack.set_White_color()

        # Thêm 1 lò xo (Stretch) ở TRÊN CÙNG để đẩy mọi thứ xuống
        layout.addStretch()
        
        self.button_blackjack.clicked.connect(self.open_blackjack_window)
        layout.addWidget(self.button_blackjack, alignment = Qt.AlignCenter)
        
        layout.addStretch()
        
        
        self.game_window = None
        
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_blackjack_window(self):
        if self.game_window is None or not self.game_window.isVisible():
            # Chú ý chữ J viết hoa giống như tên Class bên file ui.py
            self.game_window = BlackJackWindow()
            self.game_window.show()
        else:
            self.game_window.raise_()
            self.game_window.activateWindow()




# Cài đặt
class SettingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Poker App")
        self.setGeometry(100, 100, 800, 400) # x, y, width, height

        # Add content for the game screen
        container = QWidget()
        layout = QVBoxLayout()
        
       
         # Add a back button
        back_button = QPushButton("Quay lai")
        back_button.setFixedSize(100, 50)
        back_button.clicked.connect(self.close)
        layout.addWidget(back_button,alignment = Qt.AlignLeft | Qt.AlignTop)
        
        # Nội dung chính
        label = QLabel("Cài đặt")
        layout.addWidget(label)
        

       
        container.setLayout(layout)
        self.setCentralWidget(container)





# Define a function to be executed when the button is clicked (a "slot")
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Poker App")
        self.setGeometry(100, 100, 800, 400) # x, y, width, height
        
         # (2) Tải bức tranh từ file lưu trên máy vào bộ nhớ thành QPixmap
        hinh_nen = QPixmap("./file_anh/main_theme.jpg")
        
        # (Lựa chọn) Bóp nắn, kéo dãn tấm hình cho vừa in với size cửa sổ (800x400)
        hinh_nen_vua_khit = hinh_nen.scaled(self.size()) 
        # (3) Tạo một cái bảng màu (Palette), dùng công cụ Lăn Sơn (QBrush) lăn tấm hình đó lên tường
        bang_mau = self.palette()
        bang_mau.setBrush(QPalette.Window, QBrush(hinh_nen_vua_khit))
        # (4) Nộp bản sơn tường đó cho cửa sổ
        self.setPalette(bang_mau)
        # Add content for the game screen
        container=QWidget()
        layout = QVBoxLayout()
        
        
        #button1
        self.button1 = Mainbtn("Bat dau")
        self.button1.setFixedSize(200, 50)
        self.button1.set_White_color()


        #button2
        self.button2 = Mainbtn("Cai dat")
        self.button2.setFixedSize(200, 50)
        self.button2.set_White_color()


        self.game_window = None

         # Thêm 1 lò xo (Stretch) ở TRÊN CÙNG để đẩy mọi thứ xuống
        layout.addStretch()
        
        layout.addWidget(self.button1,alignment=Qt.AlignCenter)
        layout.addSpacing(20) # căn chỉnh khoảng cách giữa các button
        layout.addWidget(self.button2,alignment=Qt.AlignCenter)

        layout.addStretch()
        
        container.setLayout(layout)
        self.setCentralWidget(container)
        

        self.button1.clicked.connect(self.open_game_window)
        self.button2.clicked.connect(self.open_setting_window)

    def open_game_window(self):
        if self.game_window is None or not self.game_window.isVisible():
            self.game_window = PokerGameWindow()
            self.game_window.show()
        else:
            self.game_window.raise_()
            self.game_window.activateWindow()

    def open_setting_window(self):
        if self.game_window is None or not self.game_window.isVisible():
            self.game_window = SettingWindow()
            self.game_window.show()
        else:
            self.game_window.raise_()
            self.game_window.activateWindow()
       

# Run the application

    
   
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()   # Tạo 1 cửa sổ thôi
    window.show()           # Show lên
    sys.exit(app.exec())

    
