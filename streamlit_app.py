import streamlit as st
import streamlit.components.v1 as components

# Page config
st.set_page_config(page_title="Hay Day Farm", page_icon="🌾", layout="wide")

# Custom CSS for Hay Day theme
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
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("🌾 Hay Day Farm 🐄")
st.subheader("Welcome to your farm!")

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
        width: 100%;
        height: 100%;
        object-fit: cover;
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

# Farm sections
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌻 Crops")
    crop = st.selectbox("Plant a crop:", ["Wheat", "Corn", "Soybeans", "Carrots"])
    if st.button("🌱 Plant"):
        st.success(f"Planted {crop}!")

with col2:
    st.markdown("### 🐓 Animals")
    animal = st.selectbox("Feed animal:", ["Chicken", "Cow", "Pig", "Sheep"])
    if st.button("🥕 Feed"):
        st.success(f"Fed the {animal}!")

with col3:
    st.markdown("### 🏪 Shop")
    st.metric("Coins", "1,250", "+50")
    st.metric("Level", "15", "+1")

# Farm status
st.markdown("---")
st.info("🎯 Daily Task: Harvest 10 wheat crops!")
