# Mọi thứ chỉ cần như thế này thôi:
import sys
from file_game.black_jack.game1_black_jack import Deck, Hand


from PySide6.QtWidgets import QApplication, QSpinBox, QMessageBox, QPushButton, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Slot, Qt
from PySide6.QtGui import QPixmap





class BlackJackWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bàn chơi Blackjack")
        self.setGeometry(100, 100, 800, 700) 
        
        # MÀU NỀN MẶC ĐỊNH CHO BÀN CHƠI (Xanh lá sòng bài)
        self.setStyleSheet("QWidget { background-color: #0b5345; }")
        
        container = QWidget()
        layout_chinh = QVBoxLayout()
        
        # === 1. TẠO KHU VỰC CHỨA BÀI (LAYOUT NGANG) ===
        self.label_diem_nha_cai = QLabel("Bài Nhà Cái:")
        self.label_diem_nha_cai.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        self.khay_bai_nha_cai = QHBoxLayout()
        
        self.label_diem_nguoi_choi = QLabel("Bài Người Chơi:")
        self.label_diem_nguoi_choi.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        self.khay_bai_nguoi_choi = QHBoxLayout()

        self.label_thongbao = QLabel("CHÀO MỪNG ĐẾN CASINO!")
        self.label_thongbao.setAlignment(Qt.AlignCenter)
        self.label_thongbao.setStyleSheet("font-size: 24px; color: yellow; font-weight: bold;")

        # Thêm lò xo để ép khu bài nhà cái lên đỉnh, người chơi xuống đáy
        layout_chinh.addWidget(self.label_diem_nha_cai)
        layout_chinh.addLayout(self.khay_bai_nha_cai)
        
        layout_chinh.addStretch() # Lò xo ở giữa đẩy màn hình ra xa
        layout_chinh.addWidget(self.label_thongbao)
        layout_chinh.addStretch()
        
        layout_chinh.addWidget(self.label_diem_nguoi_choi)
        layout_chinh.addLayout(self.khay_bai_nguoi_choi)

        # KHỞI TẠO TÀI SẢN
        self.tong_tien = 5000
        self.tien_cuoc = 0

        # ==== 1.5 TẠO KHU VỰC ĐẶT CƯỢC ====
        self.khay_tien_te = QHBoxLayout()
        self.label_tien_cua_toi = QLabel(f"💰 TÀI SẢN: ${self.tong_tien}")
        self.label_tien_cua_toi.setStyleSheet("color: gold; font-size: 20px; font-weight: bold;")
        
        self.label_nhap_cuoc = QLabel("💵 Tiền Cược:")
        self.label_nhap_cuoc.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        
        # Công cụ SpinBox 
        self.o_nhap_cuoc = QSpinBox()
        self.o_nhap_cuoc.setRange(200, self.tong_tien) # Min 200, Max là Tất tay 5000
        self.o_nhap_cuoc.setSingleStep(200) # Mỗi lần bấm mũi tên thì tăng 200$
        self.o_nhap_cuoc.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.o_nhap_cuoc.setFixedSize(120, 30)

        # Trưng lên khay nằm ngang
        self.btn_all_in = QPushButton("ALL-IN")
        self.btn_all_in.setStyleSheet("background-color: darkred; color: yellow; font-size: 14px; font-weight: bold;")
        self.btn_all_in.setFixedSize(80, 30)
        self.btn_all_in.clicked.connect(self.cuoc_tat_tay)
        
        self.khay_tien_te.addWidget(self.label_tien_cua_toi)
        self.khay_tien_te.addStretch() # Lò xo đẩy tiền ra 2 góc
        self.khay_tien_te.addWidget(self.label_nhap_cuoc)
        self.khay_tien_te.addWidget(self.o_nhap_cuoc)
        self.khay_tien_te.addWidget(self.btn_all_in)
        
        layout_chinh.addLayout(self.khay_tien_te) # Gắn cả khay vào màn hình
        
        # === 2. TẠO CÁC NÚT BẤM ===
        self.lay_out_nut_bam = QHBoxLayout() # Xếp 3 nút nằm ngang cho giống thật
        self.btn_chia_bai = QPushButton("Ván Mới")
        self.btn_rut_bai = QPushButton("Rút Bài (Hit)")
        self.btn_dung_lai = QPushButton("Dừng lại (Stand)")
        self.btn_rut_bai.setEnabled(False)
        self.btn_dung_lai.setEnabled(False)
        
        for btn in [self.btn_chia_bai, self.btn_rut_bai, self.btn_dung_lai]:
            btn.setFixedSize(150, 40)
            btn.setStyleSheet("background-color: white; font-weight: bold; font-size: 14px; border-radius: 5px;")
            self.lay_out_nut_bam.addWidget(btn)

        layout_chinh.addLayout(self.lay_out_nut_bam)
        container.setLayout(layout_chinh)
        self.setCentralWidget(container)

        # === 3. KẾT NỐI NÚT VỚI BỘ NÃO ===
        self.btn_chia_bai.clicked.connect(self.start_new_game)
        self.btn_rut_bai.clicked.connect(self.player_hit)
        self.btn_dung_lai.clicked.connect(self.player_stand)

    # === CỖ MÁY DỊCH TỪ "Não" SANG "Tên Ảnh" ===
    def get_ten_file_anh(self, card):
        chuyen_chu_thuong = card.suit.lower()
        if "spades" in chuyen_chu_thuong: chat_bai = "spades"
        elif "clubs" in chuyen_chu_thuong: chat_bai = "clubs"
        elif "hearts" in chuyen_chu_thuong: chat_bai = "hearts"
        else: chat_bai = "diamonds"
        
        so_bai = card.rank.lower()
        if so_bai == "j": so_bai = "jack"
        elif so_bai == "q": so_bai = "queen"
        elif so_bai == "k": so_bai = "king"
        elif so_bai == "a": so_bai = "ace"
        
        return f"./file_anh/52_cards/playing-cards-assets-master/playing-cards-assets-master/png/{so_bai}_of_{chat_bai}.png"

    # Hành động dọn dẹp quét sạch ván bài cũ đi
    def xoa_bai_tren_mang_hinh(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    # ================= CÁC HÀM XỬ LÝ SỰ KIỆN LÕI ===================
    def start_new_game(self):
        # 1. THU TIỀN CƯỢC TRƯỚC KHI CHIA BÀI
        self.tien_cuoc = self.o_nhap_cuoc.value()
        self.tong_tien -= self.tien_cuoc # Thu tiền trong túi
        self.label_tien_cua_toi.setText(f"💰 TÀI SẢN: ${self.tong_tien}")
        
        # 2. Khóa không cho đổi ý đổi tiền hay giam nút Ván Mới
        self.o_nhap_cuoc.setEnabled(False)
        self.btn_chia_bai.setEnabled(False) 

        # 3. CHIA BÀI
        self.deck = Deck()
        self.deck.shuffle()
        self.player_hand = Hand()
        self.dealer_hand = Hand()

        self.player_hand.add_card(self.deck.deal())
        self.player_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())
        self.dealer_hand.add_card(self.deck.deal())

        self.cap_nhat_man_hinh()
        self.label_thongbao.setText(f"Đang Cược: ${self.tien_cuoc}. Rút hay Dừng?\nGợi ý của chuyên gia: Tất tay đi em 😎")
        
        self.btn_rut_bai.setEnabled(True)
        self.btn_dung_lai.setEnabled(True)

    def player_hit(self):
        self.player_hand.add_card(self.deck.deal())
        self.player_hand.adjust_for_ace()
        self.cap_nhat_man_hinh()

        # goi api den server de update thong tin boc bai
        

        if self.player_hand.value > 21:
            self.label_thongbao.setText("CẢM ƠN VÌ SỰ ĐẦU TƯ\n TIỀN CỦA BẠN SẼ DÙNG VỚI MỤC ĐÍCH TỪ THIỆN (CHO GIA ĐÌNH TÔI)")
            self.ket_thuc_van_bai()

    def player_stand(self):
        while (self.dealer_hand.value < self.player_hand.value or self.dealer_hand.value <15) and (self.dealer_hand.value < 21):
            self.dealer_hand.add_card(self.deck.deal())
            self.dealer_hand.adjust_for_ace()
        
        self.cap_nhat_man_hinh()

        # TÍNH TOÁN TIỀN TỆ TRẢ THƯỞNG
        if self.dealer_hand.value > 21 or self.dealer_hand.value <15:
            self.label_thongbao.setText("BOT QUÁ NGU, BẠN ĂN CHẶT")
            self.tong_tien += self.tien_cuoc * 2 
        elif (self.dealer_hand.value > self.player_hand.value) or self.player_hand.value >21:
            self.label_thongbao.setText("BẠN NHÓT, NHÀ CÁI ĐÃ BẮN 💦💦!")
        elif self.dealer_hand.value < self.player_hand.value:
            self.label_thongbao.setText("BẠN BÚ ĐẪM")
            self.tong_tien += self.tien_cuoc * 2
        else:
            self.label_thongbao.setText("HÒA NHAU!")
            self.tong_tien += self.tien_cuoc 
        self.ket_thuc_van_bai()

    def cap_nhat_man_hinh(self):
        self.label_diem_nguoi_choi.setText(f"Bài Người Chơi ({self.player_hand.value} điểm):")
        self.label_diem_nha_cai.setText(f"Bài Nhà Cái ({self.dealer_hand.value} điểm):")

        # 1. Quét dọn khay bài cũ trước
        self.xoa_bai_tren_mang_hinh(self.khay_bai_nguoi_choi)
        self.xoa_bai_tren_mang_hinh(self.khay_bai_nha_cai)

        # 2. Xếp Bài Cho Người Chơi (Bằng Ảnh)
        for card in self.player_hand.cards:
            hinh_nen = QPixmap(self.get_ten_file_anh(card)) 
            la_bai_mini = hinh_nen.scaledToHeight(150, Qt.SmoothTransformation) 
            
            label_hinh = QLabel() 
            label_hinh.setPixmap(la_bai_mini) 
            label_hinh.setFixedSize(la_bai_mini.width(), la_bai_mini.height())
            label_hinh.setStyleSheet("background-color: white; border-radius: 8px;")
            
            self.khay_bai_nguoi_choi.addWidget(label_hinh) 
            
        self.khay_bai_nguoi_choi.addStretch()

        # 3. Xếp Bài Cho Nhà Cái (Bằng Ảnh)
        for card in self.dealer_hand.cards:
            hinh_nen = QPixmap(self.get_ten_file_anh(card))
            la_bai_mini = hinh_nen.scaledToHeight(150, Qt.SmoothTransformation)
            
            label_hinh = QLabel()
            label_hinh.setPixmap(la_bai_mini)
            label_hinh.setFixedSize(la_bai_mini.width(), la_bai_mini.height())
            label_hinh.setStyleSheet("background-color: white; border-radius: 8px;")
            self.khay_bai_nha_cai.addWidget(label_hinh)
            
        self.khay_bai_nha_cai.addStretch()

    # Gắn vào dưới cùng tít đáy của file ui.py nhé
    def cuoc_tat_tay(self):
        # Đẩy ô SpinBox vọt phát lên kịch trần tổng tiền đang có luôn
        self.o_nhap_cuoc.setValue(self.tong_tien)

    # HÀM BÁO TỬ / TRẢ LỜI CHO MÀN HÌNH GAME OVER
    def ket_thuc_van_bai(self):
        self.label_tien_cua_toi.setText(f"💰 TÀI SẢN: ${self.tong_tien}")
        
        if self.tong_tien < 200:
            bang_phieu_phat = QMessageBox(self)
            bang_phieu_phat.setWindowTitle("LỆNH TRỤC XUẤT")
            
            # --- TÙY CHỈNH THẨM MỸ CHO CÁI MINI WINDOW NÀY ----
            bang_phieu_phat.setStyleSheet("""
                QMessageBox { 
                    background-color: #2b0000; /* Nền màu đỏ đen cực ngầu */
                } 
                QLabel { 
                    color: white; 
                    font-size: 18px; 
                    font-weight: bold; 
                } 
                QPushButton { 
                    background-color: red; 
                    color: white; 
                    font-size: 16px;
                    font-weight: bold;
                    padding: 8px 15px; 
                    border-radius: 5px;
                }
            """)
            #----------------------------------------------------
            if self.tong_tien <= 0:
                bang_phieu_phat.setIcon(QMessageBox.Critical)
                bang_phieu_phat.setText("NHÀ CÁI GHI NHẬN SỰ CỐNG HIẾN CỦA BẠN!\nGIỜ THÌ BẠN CHIM CÚT ĐƯỢC RỒI!")
            else:
                bang_phieu_phat.setIcon(QMessageBox.Warning)
                bang_phieu_phat.setText(f"BẠN CHỈ CÒN ${self.tong_tien}.\nSÒNG KHÔNG HOAN NGHÊNH BỌN KHỐ RÁCH ÁO ÔM!")
            
            # Ra lệnh cho hiển thị cái bảng lên
            bang_phieu_phat.exec()
            
            # Đóng sập cửa sổ văng ra ngoài sau khi bấm OK
            self.close() 
            return 
            
        self.o_nhap_cuoc.setRange(200, self.tong_tien) 
        self.o_nhap_cuoc.setEnabled(True)
        self.btn_chia_bai.setEnabled(True)
        
        self.btn_rut_bai.setEnabled(False)
        self.btn_dung_lai.setEnabled(False)
