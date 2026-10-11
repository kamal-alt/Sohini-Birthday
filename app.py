from datetime import datetime
import streamlit as pd_st

# Page configuration
pd_st.set_page_config(
    page_title="Counting Down for Sohini ❤️", page_icon="✨", layout="centered"
)

# Custom Styling (Romantic aesthetic)
pd_st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f3 0%, #ffccd5 100%);
    }
    h1, h2, h3 {
        color: #c9184a !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .quote-box {
        background-color: rgba(255, 255, 255, 0.85);
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(201, 24, 74, 0.1);
        text-align: center;
        margin-top: 20px;
        border-left: 5px solid #ff4d6d;
    }
    .quote-text {
        font-size: 1.2rem;
        color: #590d22;
        font-style: italic;
        line-height: 1.6;
    }
    .countdown-card {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Title section personalized for Sohini
pd_st.markdown(
    "<h1 style='text-align: center;'>Counting Down to Sohini’s Special Day ✨</h1>",
    unsafe_allow_html=True,
)
pd_st.markdown(
    "<p style='text-align: center; color: #7b2cbf; font-size: 1.1rem;'>Every second brings us closer to celebrating you, gorgeous! 💕</p>",
    unsafe_allow_html=True,
)

# Target Birthday (Nov 10, 2026)
today = datetime.now()
target_date = datetime(2026, 11, 10, 0, 0, 0)
time_remaining = target_date - today

days = time_remaining.days
hours = time_remaining.seconds // 3600
minutes = (time_remaining.seconds % 3600) // 60

# Display Countdown Metrics
col1, col2, col3 = pd_st.columns(3)
with col1:
    pd_st.markdown(
        f"<div class='countdown-card'><h3>{days}</h3><p>Days</p></div>",
        unsafe_allow_html=True,
    )
with col2:
    pd_st.markdown(
        f"<div class='countdown-card'><h3>{hours}</h3><p>Hours</p></div>",
        unsafe_allow_html=True,
    )
with col3:
    pd_st.markdown(
        f"<div class='countdown-card'><h3>{minutes}</h3><p>Minutes</p></div>",
        unsafe_allow_html=True,
    )

pd_st.markdown("<br>", unsafe_allow_html=True)

# List of daily quotes tailored for her
quotes = [
    "Sohini, I love you not only for what you are, but for what I am when I am with you.",
    "In a world full of temporary things, you are my forever favorite, Sohini.",
    "Every day with you is a new adventure and my absolute favorite part of life.",
    "Your smile is literally the brightest part of my day, every single day.",
    "I didn't choose you by accident, Sohini; loving you is the best choice I ever made.",
    "You are my today and all of my tomorrows.",
    "Just a reminder: you are incredible, gorgeous, and deeply loved.",
    "My favorite place in the entire world is right beside you.",
    "The best things in life are better with you, Sohini.",
    "Thank you for being the sweetest reason behind my smile.",
]

# Select quote based on the day of the year so it changes daily automatically
day_of_year = today.timetuple().tm_yday
today_quote = quotes[day_of_year % len(quotes)]

# Display Daily Quote
pd_st.markdown("### 💌 Today's Little Note For You")
pd_st.markdown(
    f"<div class='quote-box'><p class='quote-text'>\"{today_quote}\"</p></div>",
    unsafe_allow_html=True,
)
