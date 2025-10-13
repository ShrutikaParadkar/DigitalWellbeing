# app.py
import streamlit as st
import pandas as pd
import joblib
import numpy as np

st.set_page_config(page_title="Digital Wellbeing Analyzer", page_icon="📱", layout="wide")


# Load Trained Model

@st.cache_resource
def load_model():
    model = joblib.load("burnout_model.pkl")  # must exist in same folder
    return model

model = load_model()

# Streamlit UI

st.title("📱 Digital Wellbeing Pattern Analyzer")
st.write("Analyze your smartphone usage patterns and get personalized recommendations.")

# Collect user inputs
st.sidebar.header("User Profile")
age = st.sidebar.slider("Age", 15, 70, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female", "Other"])
profession = st.sidebar.selectbox("Profession", ["Student", "IT Professional", "Healthcare", "Education", "Other"])
city_tier = st.sidebar.selectbox("City Tier", ["Tier 1", "Tier 2", "Tier 3"])

st.sidebar.header("Daily Usage")
daily_screen_time_min = st.sidebar.slider("Daily Screen Time (minutes)", 60, 900, 300)
sleep_hours = st.sidebar.slider("Sleep Hours", 3, 12, 7)
social_media_time_min = st.sidebar.slider("Social Media Usage (minutes)", 0, 600, 120)
anxiety_level = st.sidebar.slider("Anxiety Level (0-10)", 0, 10, 3)
focus_score = st.sidebar.slider("Focus Score (0-10)", 0, 10, 6)
mood_score = st.sidebar.slider("Mood Score (0-10)", 0, 10, 7)

# Derived features
social_media_ratio = social_media_time_min / (daily_screen_time_min + 1)

# Build input row
input_row = pd.DataFrame([{
    "age": age,
    "gender": gender,
    "profession": profession,
    "city_tier": city_tier,
    "daily_screen_time_min": daily_screen_time_min,
    "sleep_hours": sleep_hours,
    "social_media_time_min": social_media_time_min,
    "anxiety_level": anxiety_level,
    "focus_score": focus_score,
    "mood_score": mood_score,
    "social_media_ratio": social_media_ratio,
}])

# Prediction

if st.button("Get My Recommendations"):
    try:
        prediction = model.predict(input_row)[0]
        prediction_proba = model.predict_proba(input_row)[0]

        st.subheader("🔮 Prediction Result")
        if prediction == 1:
            st.error("⚠️ High risk of digital burnout detected!")
        else:
            st.success("✅ No significant burnout risk detected.")

        st.write(f"**Model Confidence:** {prediction_proba[prediction]*100:.2f}%")

        
        # Recommendations
        
        st.subheader("💡 Personalized Recommendations")

        recommendations = []
        if daily_screen_time_min > 360:
            recommendations.append("📉 Reduce overall screen time below 6 hours/day.")
        if social_media_ratio > 0.4:
            recommendations.append("📱 Limit social media use to under 30% of screen time.")
        if sleep_hours < 6:
            recommendations.append("😴 Improve sleep hygiene (aim for 7–8 hours).")
        if anxiety_level >= 7:
            recommendations.append("🧘 Practice relaxation techniques to manage anxiety.")
        if focus_score < 5:
            recommendations.append("🎯 Use focus apps or Pomodoro technique to improve focus.")
        if mood_score < 5:
            recommendations.append("🌱 Engage in offline hobbies and physical activities.")

        if not recommendations:
            recommendations.append("🎉 Keep up your healthy digital habits!")

        for rec in recommendations:
            st.write(f"- {rec}")

    except Exception as e:
        st.error(f"Error while predicting: {e}")

