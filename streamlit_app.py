import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Farm Tic-Tac-Toe", page_icon="🌾", layout="wide")

# Initialize session state for tic-tac-toe
if 'board' not in st.session_state:
    st.session_state.board = [''] * 9
if 'current_player' not in st.session_state:
    st.session_state.current_player = '🌾'  # Wheat for player 1
if 'winner' not in st.session_state:
    st.session_state.winner = None
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #FFF8DC;
    }
    .stButton>button {
        background-color: #FFFACD;
        color: black;
        font-weight: bold;
        font-size: 80px;
        height: 150px;
        width: 100%;
        border-radius: 15px;
        border: 4px solid #8B4513;
    }
    .stButton>button:hover {
        background-color: #FFEC8B;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🌾 Farm Tic-Tac-Toe 🐄")
st.subheader("Player 1: 🌾 Wheat | Player 2: 🐄 Cow")

# Jumpscare HTML/CSS/JS
jumpscare_html = """
<style>
    #jumpscare {
        display: none;
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: black;
        z-index: 9999;
        justify-content: center;
        align-items: center;
        animation: shake 0.1s infinite;
    }
    #jumpscare img {
        max-width: 100%;
        max-height: 100%;
        object-fit: contain;
    }
    @keyframes shake {
        0%, 100% { transform: translate(0, 0) rotate(0deg); }
        25% { transform: translate(-5px, 5px) rotate(-2deg); }
        50% { transform: translate(5px, -5px) rotate(2deg); }
        75% { transform: translate(-5px, -5px) rotate(-1deg); }
    }
    .scare-btn {
        background: linear-gradient(45deg, #8B4513, #D2691E);
        color: white;
        border: none;
        padding: 15px 30px;
        font-size: 18px;
        border-radius: 10px;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0,0,0,0.3);
        transition: all 0.3s;
    }
    .scare-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 8px rgba(0,0,0,0.4);
    }
</style>

<div id="jumpscare">
    <img src="https://media.tenor.com/vTd_I2Dpiz0AAAAM/conbopongcuoi.gif" alt="scary">
</div>

<center>
    <button class="scare-btn" onclick="triggerJumpscare()">🎃 Mystery Box 🎃</button>
</center>

<script>
    function triggerJumpscare() {
        const scare = document.getElementById('jumpscare');
        scare.style.display = 'flex';
        
        // Create audio element for scream
        const scream = new Audio('https://www.myinstants.com/media/sounds/scary-scream.mp3');
        scream.play();
        
        setTimeout(() => {
            scare.style.display = 'none';
        }, 3000);
    }
</script>
"""

components.html(jumpscare_html, height=150)

# Game functions
def check_winner():
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    
    for combo in winning_combinations:
        if (st.session_state.board[combo[0]] == st.session_state.board[combo[1]] == 
            st.session_state.board[combo[2]] != ''):
            return st.session_state.board[combo[0]]
    
    if '' not in st.session_state.board:
        return 'Draw'
    
    return None

def reset_game():
    st.session_state.board = [''] * 9
    st.session_state.current_player = '🌾'
    st.session_state.winner = None
    st.session_state.game_over = False

def make_move(index):
    if not st.session_state.game_over and st.session_state.board[index] == '':
        st.session_state.board[index] = st.session_state.current_player
        winner = check_winner()
        
        if winner:
            st.session_state.winner = winner
            st.session_state.game_over = True
        else:
            st.session_state.current_player = '🐄' if st.session_state.current_player == '🌾' else '🌾'

# Game status
st.markdown("---")
if st.session_state.game_over:
    if st.session_state.winner == 'Draw':
        st.warning("🤝 It's a Draw!")
    else:
        st.balloons()
        winner_name = "Player 1 (🌾 Wheat)" if st.session_state.winner == '🌾' else "Player 2 (🐄 Cow)"
        st.success(f"🎉 {winner_name} WINS! 🎉")
else:
    player_name = "Player 1's turn (🌾 Wheat)" if st.session_state.current_player == '🌾' else "Player 2's turn (🐄 Cow)"
    st.info(f"🎮 {player_name}")

if st.button("🔄 New Game", key="reset"):
    reset_game()
    st.rerun()

st.markdown("---")

# Tic-Tac-Toe Board
st.markdown("### 🎯 Game Board")
for row in range(3):
    cols = st.columns(3)
    for col in range(3):
        index = row * 3 + col
        with cols[col]:
            button_label = st.session_state.board[index] if st.session_state.board[index] else '🟫'
            if st.button(button_label, key=f"cell_{index}", disabled=st.session_state.game_over or st.session_state.board[index] != ''):
                make_move(index)
                st.rerun()

st.markdown("---")
st.info("📋 Rules: Get 3 in a row (horizontal, vertical, or diagonal) to win!")
