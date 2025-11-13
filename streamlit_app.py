import streamlit as st
import streamlit.components.v1 as components
import random

# Page config
st.set_page_config(page_title="Farm Battle - 2 Players", page_icon="🎮", layout="wide")

# Initialize session state for game
if 'player1_score' not in st.session_state:
    st.session_state.player1_score = 0
if 'player2_score' not in st.session_state:
    st.session_state.player2_score = 0
if 'game_round' not in st.session_state:
    st.session_state.game_round = 1

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #87CEEB;
    }
    .stButton>button {
        background-color: #FFD700;
        color: #8B4513;
        font-weight: bold;
        border-radius: 10px;
        width: 100%;
    }
    .player1-section {
        border: 3px solid #FF6B6B;
        padding: 20px;
        border-radius: 15px;
        background-color: rgba(255, 107, 107, 0.1);
    }
    .player2-section {
        border: 3px solid #4ECDC4;
        padding: 20px;
        border-radius: 15px;
        background-color: rgba(78, 205, 196, 0.1);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🎮 Farm Battle - 2 Players 🎮")
st.subheader(f"Round {st.session_state.game_round} | Race to 100 points!")

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

# Score Display
st.markdown("---")
score_col1, score_col2, score_col3 = st.columns([1, 1, 1])
with score_col1:
    st.metric("🔴 Player 1", f"{st.session_state.player1_score} points")
with score_col2:
    if st.button("🔄 Reset Game"):
        st.session_state.player1_score = 0
        st.session_state.player2_score = 0
        st.session_state.game_round = 1
        st.rerun()
with score_col3:
    st.metric("🔵 Player 2", f"{st.session_state.player2_score} points")

st.markdown("---")

# Player sections
p1_col, p2_col = st.columns(2)

with p1_col:
    st.markdown('<div class="player1-section">', unsafe_allow_html=True)
    st.markdown("### 🔴 PLAYER 1")
    
    st.markdown("#### 🌾 Harvest Crops")
    if st.button("🌻 Harvest Wheat", key="p1_wheat"):
        points = random.randint(5, 15)
        st.session_state.player1_score += points
        st.success(f"Harvested! +{points} points")
        st.session_state.game_round += 1
        st.rerun()
    
    if st.button("🌽 Harvest Corn", key="p1_corn"):
        points = random.randint(10, 20)
        st.session_state.player1_score += points
        st.success(f"Harvested! +{points} points")
        st.session_state.game_round += 1
        st.rerun()
    
    st.markdown("#### 🐓 Feed Animals")
    if st.button("🐔 Feed Chicken", key="p1_chicken"):
        points = random.randint(3, 8)
        st.session_state.player1_score += points
        st.success(f"Fed! +{points} points")
        st.session_state.game_round += 1
        st.rerun()
    
    if st.button("🐄 Feed Cow", key="p1_cow"):
        points = random.randint(8, 12)
        st.session_state.player1_score += points
        st.success(f"Fed! +{points} points")
        st.session_state.game_round += 1
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

with p2_col:
    st.markdown('<div class="player2-section">', unsafe_allow_html=True)
    st.markdown("### 🔵 PLAYER 2")
    
    st.markdown("#### 🌾 Harvest Crops")
    if st.button("🌻 Harvest Wheat", key="p2_wheat"):
        points = random.randint(5, 15)
        st.session_state.player2_score += points
        st.success(f"Harvested! +{points} points")
        st.session_state.game_round += 1
        st.rerun()
    
    if st.button("🌽 Harvest Corn", key="p2_corn"):
        points = random.randint(10, 20)
        st.session_state.player2_score += points
        st.success(f"Harvested! +{points} points")
        st.session_state.game_round += 1
        st.rerun()
    
    st.markdown("#### 🐓 Feed Animals")
    if st.button("🐔 Feed Chicken", key="p2_chicken"):
        points = random.randint(3, 8)
        st.session_state.player2_score += points
        st.success(f"Fed! +{points} points")
        st.session_state.game_round += 1
        st.rerun()
    
    if st.button("🐄 Feed Cow", key="p2_cow"):
        points = random.randint(8, 12)
        st.session_state.player2_score += points
        st.success(f"Fed! +{points} points")
        st.session_state.game_round += 1
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Check for winner
st.markdown("---")
if st.session_state.player1_score >= 100:
    st.balloons()
    st.success("🎉 PLAYER 1 WINS! 🎉")
    st.markdown(f"**Final Score:** Player 1: {st.session_state.player1_score} | Player 2: {st.session_state.player2_score}")
elif st.session_state.player2_score >= 100:
    st.balloons()
    st.success("🎉 PLAYER 2 WINS! 🎉")
    st.markdown(f"**Final Score:** Player 1: {st.session_state.player1_score} | Player 2: {st.session_state.player2_score}")
else:
    st.info("🎯 First player to reach 100 points wins!")
