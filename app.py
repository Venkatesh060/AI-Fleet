import streamlit as st
import google.generativeai as genai
import time

# Set page config FIRST
st.set_page_config(page_title="StudBud", page_icon="📚", layout="centered")

# Configure Gemini API
genai.configure(api_key="AIzaSyA-fXjMcTduld5PzZ8emSbaTrFHDFOan_s")

# Initialize Gemini model
model = genai.GenerativeModel('gemini-1.5-flash')

# Function to generate study plan
def generate_study_plan(goal, strengths, weaknesses, preferences):
    prompt = f"""
    Create a personalized study plan for a student with the following details:
    - Goal: {goal}
    - Strengths: {strengths}
    - Weaknesses: {weaknesses}
    - Preferences: {preferences}

    The study plan should include:
    1. A breakdown of topics to study.
    2. A suggested schedule with time allocation.
    3. Tips for improving weak areas.
    4. Recommendations for study resources.
    """
    response = model.generate_content(prompt)
    return response.text

# Custom CSS for styling
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
    }
    .stButton button:hover {
        background-color: #45a049;
    }
    .stTextInput input, .stTextArea textarea {
        border-radius: 8px;
        border: 1px solid #ccc;
        padding: 8px;
    }
    .stMarkdown h1 {
        color: #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header
st.title("📚 StudBud: AI Study Planner")
st.markdown("🌟 Welcome to StudBud! Let's create your personalized study plan.")

# Input fields in columns
col1, col2 = st.columns(2)

with col1:
    goal = st.text_input("🎯 What is your academic goal?")
    strengths = st.text_area("💪 What are your strengths?")

with col2:
    weaknesses = st.text_area("🤔 What are your weaknesses?")
    preferences = st.text_area("⏰ What are your study preferences?")

# Generate study plan
if st.button("🚀 Generate Study Plan"):
    with st.spinner("Generating your personalized study plan..."):
        time.sleep(2)  # Simulate processing time
        study_plan = generate_study_plan(goal, strengths, weaknesses, preferences)
        st.success("✅ Study plan generated successfully!")
        st.write(study_plan)

# Progress tracking
st.subheader("📊 Your Progress")

# Initialize tasks in session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

# Add a new task
with st.form("add_task_form"):
    new_task = st.text_input("Add a new task")
    add_task_button = st.form_submit_button("Add Task")

    if add_task_button and new_task:
        st.session_state.tasks.append({"name": new_task, "completed": False})

# Display tasks with checkboxes
for i, task in enumerate(st.session_state.tasks):
    if st.checkbox(task["name"], value=task["completed"], key=f"task_{i}"):
        st.session_state.tasks[i]["completed"] = True
    else:
        st.session_state.tasks[i]["completed"] = False

# Calculate progress
total_tasks = len(st.session_state.tasks)
completed_tasks = sum(1 for task in st.session_state.tasks if task["completed"])
progress_value = (completed_tasks / total_tasks) if total_tasks > 0 else 0  # Value between 0.0 and 1.0
st.progress(progress_value)

# Display task list
st.write("📋 Your Tasks:")
for task in st.session_state.tasks:
    status = "✅" if task["completed"] else "❌"
    st.write(f"{status} {task['name']}")

# Badges and achievements
st.write("🎖️ Badges:")
if progress_value >= 0.25:  # 25%
    st.write("🏅 Beginner (Complete 25% of tasks)")
if progress_value >= 0.5:  # 50%
    st.write("🥈 Intermediate (Complete 50% of tasks)")
if progress_value >= 0.75:  # 75%
    st.write("🥇 Advanced (Complete 75% of tasks)")
if progress_value == 1.0:  # 100%
    st.write("🎉 Champion (All tasks completed!)")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by AI Fleet Team")