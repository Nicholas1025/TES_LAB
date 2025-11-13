import streamlit as st

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
