from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# 1. Nhập (Import) Bộ não Back-end vào API
from file_game.black_jack.game1_black_jack import Deck, Hand

app = FastAPI()

# Biến tạm lưu ván game (Vì Backend phải "Nhớ" ván bài đang chơi)
game_sessions = {}

# 2. Định nghĩa API: Tạo ván mới
@app.post("/api/game/start")
async def start_game(player_name: str):
    # Dùng Logic của Blackjack để tạo bộ bài
    bo_bai = Deck()
    bo_bai.shuffle()
    
    # Tạo tay bài cho người chơi và nhà cái
    player_hand = Hand()
    dealer_hand = Hand()
    
    # Chia mỗi người 2 lá khởi đầu
    player_hand.add_card(bo_bai.deal())
    dealer_hand.add_card(bo_bai.deal())
    player_hand.add_card(bo_bai.deal())
    dealer_hand.add_card(bo_bai.deal())
    
    # Lưu vào Server
    game_sessions[player_name] = {
        "deck": bo_bai,
        "player": player_hand,
        "dealer": dealer_hand
    }
    
    # Trả kết quả (Lá bài là Object nên ta lấy chữ ra bằng __str__)
    return {
        "message": "Game started!",
        "player_cards": [str(card) for card in player_hand.cards],
        "player_score": player_hand.value
    }

# 3. Định nghĩa API: Người chơi xin rút bài (Hit)
@app.post("/api/game/hit")
async def hit(player_name: str):
    if player_name not in game_sessions:
        raise HTTPException(status_code=404, detail="Game chưa bắt đầu!")
        
    van_game = game_sessions[player_name]
    
    # Rút lá mới từ bộ bài chuẩn
    la_bai_moi = van_game["deck"].deal()
    van_game["player"].add_card(la_bai_moi)
    van_game["player"].adjust_for_ace()
    
    return {
        "card_drawn": str(la_bai_moi),
        "new_score": van_game["player"].value,
        "busted": van_game["player"].value > 21
    }
