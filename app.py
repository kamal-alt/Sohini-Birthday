from datetime import datetime
import streamlit as pd_st

# Page configuration
pd_st.set_page_config(
    page_title="Counting Down for Sohini ❤️", page_icon="✨", layout="centered"
)

# Custom Styling for a gorgeous mobile-friendly look
pd_st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #fff0f3 0%, #ffccd5 100%);
    }
    h1 {
        color: #c9184a !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 1.5rem !important;
        text-align: center;
    }
    .subtitle {
        color: #7b2cbf;
        font-size: 0.95rem;
        text-align: center;
        margin-bottom: 25px;
    }
    .quote-box {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(201, 24, 74, 0.1);
        text-align: center;
        margin-top: 25px;
        border-left: 5px solid #ff4d6d;
    }
    .quote-text {
        font-size: 1.05rem;
        color: #590d22;
        font-style: italic;
        line-height: 1.5;
    }
    /* Compact horizontal countdown layout for mobile */
    .countdown-container {
        display: flex;
        justify-content: center;
        gap: 10px;
        margin-bottom: 10px;
    }
    .countdown-card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 12px 10px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        flex: 1;
        max-width: 100px;
    }
    .countdown-number {
        font-size: 1.3rem;
        font-weight: bold;
        color: #c9184a;
        margin: 0;
    }
    .countdown-label {
        font-size: 0.75rem;
        color: #590d22;
        text-transform: uppercase;
        margin: 4px 0 0 0;
        letter-spacing: 0.5px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Title section personalized for Sohini
pd_st.markdown(
    "<h1>Counting Down to Sohini’s Special Day ✨</h1>", unsafe_allow_html=True
)
pd_st.markdown(
    "<p class='subtitle'>Every second brings us closer to celebrating you, gorgeous! 💕</p>",
    unsafe_allow_html=True,
)

# Target Birthday (Nov 10, 2026)
today = datetime.now()
target_date = datetime(2026, 11, 10, 0, 0, 0)
time_remaining = target_date - today

days = time_remaining.days
hours = time_remaining.seconds // 3600
minutes = (time_remaining.seconds % 3600) // 60

# Display Clean Horizontal Countdown
pd_st.markdown(
    f"""
    <div class="countdown-container">
        <div class="countdown-card">
            <p class="countdown-number">{days}</p>
            <p class="countdown-label">Days</p>
        </div>
        <div class="countdown-card">
            <p class="countdown-number">{hours}</p>
            <p class="countdown-label">Hours</p>
        </div>
        <div class="countdown-card">
            <p class="countdown-number">{minutes}</p>
            <p class="countdown-label">Minutes</p>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

# List of 30 unique daily quotes
quotes = [
    "I love you not only for what you are, but for what I am when I am with you.",
    "In a world full of temporary things, you are my forever favorite.",
    "Every day with you is a new adventure and my absolute favorite part of life.",
    "Your smile is literally the brightest part of my day, every single day.",
    "I didn't choose you by accident; loving you is the best choice I ever made.",
    "You are my today and all of my tomorrows.",
    "Just a reminder: you are incredible, gorgeous, and deeply loved.",
    "My favorite place in the entire world is right beside you.",
    "The best things in life are better with you.",
    "Thank you for being the sweetest reason behind my smile.",
    "If I had a flower for every time I thought of you, I could walk in my garden forever.",
    "I look at you and I see the rest of my life in front of my eyes.",
    "Whatever our souls are made of, yours and mine are the same.",
    "You're the first thing I think about when I wake up and the last thing before I fall asleep.",
    "Loving you is effortless because you make every single day brighter.",
    "Holding your hand is my favorite way to walk through the world.",
    "You are my sun, my moon, and all of my stars.",
    "There is no remedy for love, but to love more.",
    "To the world you may be one person, but to me you are the world.",
    "I never knew what it meant to truly miss someone until you walked into my life.",
    "You make my heart skip a beat without even trying.",
    "Every love story is beautiful, but ours is my absolute favorite.",
    "You are the best plot twist I could have ever asked for.",
    "Being deeply loved by you gives me strength, while loving you gives me courage.",
    "My heart is, and always will be, yours.",
    "I still fall for you a little bit more every single day.",
    "You are the thought that turns a bad day into a good one instantly.",
    "Life with you feels like a warm embrace on a chilly evening.",
    "I didn't know home could be a person until I found you.",
    "Counting down the days until we celebrate you, because you deserve the world.",
]

# Select quote based on the day of the year
day_of_year = today.timetuple().tm_yday
today_quote = quotes[day_of_year % len(quotes)]

# Display Daily Quote
pd_st.markdown(
    "<h3 style='text-align: center; color: #c9184a; font-size: 1.2rem; margin-top: 25px;'>💌 Today's Little Note For You</h3>",
    unsafe_allow_html=True,
)
pd_st.markdown(
    f"<div class='quote-box'><p class='quote-text'>\"{today_quote}\"</p></div>",
    unsafe_allow_html=True,
)
