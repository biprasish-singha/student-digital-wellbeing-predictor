import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import math

# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(page_title="Digital Wellbeing Predictor", page_icon="🧠", layout="centered")

# ============================================================
# FUNCTION TO LOAD TRAINED MODELS AND RESULTS
# ============================================================

@st.cache_resource
def load_models():
    stress_model = joblib.load("stress_level_model.pkl")
    mhs_model = joblib.load("mental_health_score_model.pkl")
    return stress_model, mhs_model
stress_model, mhs_model = load_models()

def add_needle(fig, value, min_value, max_value, needle_color="#222222", needle_length=0.72):
    value = max(min_value, min(max_value, float(value)))
    angle = math.pi * (1 - (value - min_value) / (max_value - min_value))
    needle_x = needle_length * math.cos(angle)
    needle_y = needle_length * math.sin(angle)
    fig.add_annotation(x=needle_x, y=needle_y, ax=0, ay=0, xref="x", yref="y", axref="x", ayref="y", showarrow=True,
                       arrowhead=3, arrowsize=1.3, arrowwidth=5, arrowcolor=needle_color)
    fig.add_shape(type="circle", xref="x", yref="y", x0=-0.055, y0=-0.055, x1=0.055, y1=0.055, fillcolor=needle_color, 
                  line={"color": needle_color, "width": 1})
    fig.update_layout(xaxis={"range": [-1, 1], "visible": False, "fixedrange": True},
                      yaxis={"range": [-0.15, 1], "visible": False, "fixedrange": True, "scaleanchor": "x", 
                             "scaleratio": 1})
    return fig

def stress_gauge(stress_level):
    stress_values = {"Low": 1, "Medium": 2, "High": 3, "Very High": 4}
    stress_level = str(stress_level).strip()
    value = stress_values[stress_level]
    fig_stress = go.Figure(go.Indicator(mode="gauge", value=value, 
                                 number={"suffix": f"-{stress_level}", "font": {"size":28}}, 
                                 title={ "text": "Stress Level", "font": {"size": 20}, "align": "center"},
                                 gauge={"axis": {"range": [0.5, 4.5], "tickvals": [1, 2, 3, 4], 
                                                 "ticktext": ["Low", "Medium", "High", "Very High"], "tickwidth": 1},
                                        "bar": {"color": "rgba(0,0,0,0)", "thickness": 0}, 
                                        "steps": [{"range": [0.5, 1.5], "color": "#2ECC71"}, 
                                                  {"range": [1.5, 2.5], "color": "#F1C40F"},
                                                  {"range": [2.5, 3.5], "color": "#E67E22"},
                                                  {"range": [3.5, 4.5], "color": "#E74C3C"}], 
                                        "borderwidth": 1, "bordercolor": "#D0D0D0"}))
    add_needle(fig=fig_stress, value=value, min_value=0.5, max_value=4.5, needle_color="red", needle_length=0.72)
    fig_stress.update_layout(height=220, margin=dict(l=20, r=20, t=45, b=10))
    return fig_stress

def mhs_gauge(mhs_score):
    mhs_score = max(0, min(10, float(mhs_score)))
    fig_mhs = go.Figure(go.Indicator(mode="gauge", value=mhs_score,
                                     number={"valueformat": ".1f", "suffix": " / 10", "font": {"size": 28}},
                                     title={"text": "Mental Health Score", "font": {"size": 20}, "align": "center"},
                                     gauge={"axis": {"range": [0, 10], "tickvals": list(range(0, 11)), "tickwidth": 1},
                                            "bar": {"color": "rgba(0,0,0,0)", "thickness": 0},
                                            "steps": [{"range": [0, 3], "color": "#E74C3C"},
                                                      {"range": [3, 5], "color": "#E67E22"},
                                                      {"range": [5, 7], "color": "#F1C40F"},
                                                      {"range": [7, 10], "color": "#2ECC71"}],
                                            "borderwidth": 1, "bordercolor": "#D0D0D0"}))
    add_needle(fig=fig_mhs, value=mhs_score, min_value=0, max_value=10, needle_color="red", needle_length=0.72)
    fig_mhs.update_layout(height=220, margin=dict(l=20, r=20, t=45, b=10))
    return fig_mhs

# ============================================================
# APPLICATION HEADER
# ============================================================

st.title("🧠 Digital Wellbeing Predictor")

st.write( """ Enter demographic, digital usage, and lifestyle information to estimate **Stress Level** and **Mental Health Score**. """)

# ============================================================
# PERSONAL / ACADEMIC INFORMATION
# ============================================================

st.subheader("👤 Personal Information")
age = st.slider("Age", 18, 30, 18)

gender = st.selectbox("Gender", ["Male", "Female"])

country = st.selectbox("Country", ["Canada", "USA", "India", "Australia", "UK", "Germany", "Bangladesh", "Brazil", 
                                   "Japan", "South Korea", "France", "Spain", "Italy", "Mexico", "Russia", "China",
                                   "Denmark", "Netherlands", "Switzerland", "Ireland", "New Zealand", "Singapore",
                                   "Malaysia", "Turkey", "UAE", "Finland", "Poland", "Pakistan", "Nepal", "Sri Lanka",
                                   "Maldives", "Other"])

academic_level = st.selectbox("Academic Level", ["Undergraduate", "Graduate", "High School"])

# ============================================================
# DIGITAL USAGE
# ============================================================

st.subheader("📱 Digital Usage")
most_used_platform = st.selectbox("Most Used Platform", ["Facebook", "LinkedIn", "Instagram", "Snapchat", "Twitter", 
                                                         "YouTube", "TikTok", "LINE", "KakaoTalk", "VKontakte", 
                                                         "WhatsApp", "WeChat"])

purpose_of_use = st.selectbox("Purpose of Use", ["Networking", "Education", "Entertainment", "News"])

avg_daily_usage = st.slider("Average Daily Usage Hours", 0.1, 16.0, 5.0)

daily_unlocks = st.slider("Daily Unlocks", 50, 300, 150)

# ============================================================
# LIFESTYLE
# ============================================================

st.subheader("📚 Lifestyle")

study_hours = st.slider("Study Hours Per Day", 0.0, 14.0, 3.0)

physical_activity_hours = st.slider("Physical Activity Hours Per Day", 0.0, 14.0, 1.0)

sleep_hours = st.slider("Sleep Hours Per Night", 0.0, 14.0, 7.0)

# ============================================================
# PREDICTION
# ============================================================

st.divider()
if st.button( "Predict", type="primary", use_container_width=True):
    non_screen_hours = 24 - avg_daily_usage
    if non_screen_hours > 0:
        screen_nonscreen_ratio = (avg_daily_usage / non_screen_hours)
    else:
        screen_nonscreen_ratio = 0
    if avg_daily_usage > 0:
        unlocks_per_usage_hour = (daily_unlocks / avg_daily_usage)
    else:
        unlocks_per_usage_hour = 0
        
    input_data = pd.DataFrame({"Age": [age], "Gender": [gender], "Country": [country],  "Academic_Level": [academic_level],
                               "Most_Used_Platform": [most_used_platform], "Purpose_Of_Use": [purpose_of_use],
                               "Avg_Daily_Usage_Hours": [avg_daily_usage], "Daily_Unlocks": [daily_unlocks], 
                               "Study_Hours": [study_hours], "Physical_Activity_Hours": [physical_activity_hours], 
                               "Sleep_Hours_Per_Night": [sleep_hours], "Screen_Nonscreen_Ratio": [screen_nonscreen_ratio],
                               "Unlocks_Per_Usage_Hour": [unlocks_per_usage_hour]})

    try:
        stress_prediction = stress_model.predict(input_data)[0]
        mhs_prediction = mhs_model.predict(input_data)[0]
        st.success("Prediction completed successfully.")
        st.subheader("Prediction Results")
        col1, col2 = st.columns(2)
        with col1:
            st.plotly_chart(stress_gauge(str(stress_prediction)), use_container_width=True)
        with col2:
            st.plotly_chart(mhs_gauge(mhs_prediction), use_container_width=True)

    except Exception as e:
        st.error(f"Prediction failed: {e}")

# ============================================================
# DISCLAIMER
# ============================================================

st.divider()
st.caption("This application demonstrates machine-learning predictions based on the dataset used to train the models and should not be interpreted as a clinical assessment.")