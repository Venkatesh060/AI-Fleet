import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API Key
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Initialize Model
model = genai.GenerativeModel("gemini-pro")

# Apply Custom CSS
st.markdown("<style>{}</style>".format(open("styles.css").read()), unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("assets/logo.png", width=200)
st.sidebar.title("📚 StudBud AI")
page = st.sidebar.radio("Navigation", ["📖 Study Plan", "📊 Progress Tracker", "⏰ Set Reminders"])

# --- STUDY PLAN PAGE ---
if page == "📖 Study Plan":
    st.title("📖 AI-Powered Study Plan")
    topic = st.text_input("Enter your study topic:")
    
    if st.button("Generate Plan 🎯"):
        if topic:
            response = model.generate_content(f"Create a structured study plan for {topic}")
            st.success("✅ Study Plan Generated!")
            st.markdown(response.text)
        else:
            st.warning("Please enter a study topic!")

# --- PROGRESS TRACKER PAGE ---
elif page == "📊 Progress Tracker":
    st.title("📊 Track Your Study Progress")
    progress = st.slider("How much have you completed?", 0, 100, 50)
    st.progress(progress / 100)
    st.write(f"📖 You have completed {progress}% of your study plan.")

# --- STUDY REMINDERS PAGE ---
elif page == "⏰ Set Reminders":
    st.title("⏰ Study Reminders")
    reminder = st.text_input("Set a reminder:")
    if st.button("Save Reminder"):
        st.success(f"✅ Reminder set: {reminder}")
