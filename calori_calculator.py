import streamlit as st

# ---------------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------------
st.set_page_config(
    page_title="CalorieFit",
    page_icon="🔥",
    layout="wide"
)

# ---------------------------------------------------------
# SESSION STATE
# ---------------------------------------------------------
if "calculated" not in st.session_state:
    st.session_state.calculated = False

# ---------------------------------------------------------
# CUSTOM STYLING
# ---------------------------------------------------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #eefcf5 0%,
            #f7fbff 45%,
            #fff8ed 100%
        );
    }

    /* Main content width */
    .block-container {
        max-width: 1150px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    /* Remove excessive top gap */
    header {
        visibility: hidden;
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        color: #173b32;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #60746d;
        margin-bottom: 30px;
    }

    /* Section headings */
    .section-title {
        font-size: 22px;
        font-weight: 750;
        color: #173b32;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    /* Metric cards */
    .metric-box {
        background: rgba(255,255,255,0.85);
        border-radius: 18px;
        padding: 20px;
        border: 1px solid #dceee7;
        text-align: center;
        box-shadow: 0 8px 25px rgba(30, 80, 65, 0.07);
    }

    .metric-label {
        font-size: 14px;
        color: #71847d;
        margin-bottom: 7px;
    }

    .metric-value {
        font-size: 28px;
        font-weight: 800;
        color: #16805c;
    }

    .metric-unit {
        font-size: 13px;
        color: #71847d;
    }

    /* Result area */
    .result-card {
        background: linear-gradient(135deg, #173f35, #1f7356);
        border-radius: 24px;
        padding: 30px;
        color: white;
        box-shadow: 0 15px 35px rgba(23, 63, 53, 0.18);
        margin-top: 20px;
    }

    .result-label {
        font-size: 15px;
        opacity: 0.85;
    }

    .result-number {
        font-size: 48px;
        font-weight: 850;
        margin: 5px 0;
    }

    .result-unit {
        font-size: 15px;
        opacity: 0.8;
    }

    /* Info box */
    .info-card {
        background: #fffaf0;
        border: 1px solid #f2dfb2;
        border-radius: 18px;
        padding: 20px;
        margin-top: 18px;
        color: #5e4c2b;
    }

    /* Tip card */
    .tip-card {
        background: #eef8ff;
        border: 1px solid #cce5f7;
        border-radius: 18px;
        padding: 20px;
        margin-top: 15px;
        color: #34536a;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 48px;
        font-weight: 700;
        border: none;
        background: #16805c;
        color: white;
    }

    .stButton > button:hover {
        background: #116b4c;
        color: white;
    }

    /* Inputs */
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        border-radius: 10px;
    }

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------
st.markdown(
    '<div class="main-title">🔥CalorieFit</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Understand your daily calorie needs and build a smarter nutrition routine.'
    '</div>',
    unsafe_allow_html=True
)

# ---------------------------------------------------------
# TOP DASHBOARD
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-label">Calculation Method</div>
        <div class="metric-value">Mifflin</div>
        <div class="metric-unit">BMR Formula</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-label">Goal Planning</div>
        <div class="metric-value">3 Goals</div>
        <div class="metric-unit">Maintain • Lose • Gain</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-label">Output</div>
        <div class="metric-value">Daily</div>
        <div class="metric-unit">Calorie Estimate</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ---------------------------------------------------------
# INPUT + RESULT LAYOUT
# ---------------------------------------------------------
left, right = st.columns([1.15, 0.85], gap="large")

# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------
with left:

    st.markdown(
        '<div class="section-title">👤 Your Personal Details</div>',
        unsafe_allow_html=True
    )

    gender = st.radio(
        "Gender",
        ["Male", "Female"],
        horizontal=True
    )

    age = st.number_input(
        "Age",
        min_value=10,
        max_value=100,
        value=25,
        step=1
    )

    col_a, col_b = st.columns(2)

    with col_a:
        weight = st.number_input(
            "Weight (kg)",
            min_value=20.0,
            max_value=300.0,
            value=65.0,
            step=0.5
        )

    with col_b:
        height = st.number_input(
            "Height (cm)",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
            step=0.5
        )

    st.markdown(
        '<div class="section-title">🏃 Activity Level</div>',
        unsafe_allow_html=True
    )

    activity = st.selectbox(
        "Choose your typical activity level",
        [
            "Sedentary — little or no exercise",
            "Lightly Active — exercise 1–3 days/week",
            "Moderately Active — exercise 3–5 days/week",
            "Very Active — exercise 6–7 days/week",
            "Extra Active — intense training / physical job"
        ]
    )

    st.markdown(
        '<div class="section-title">🎯 Your Goal</div>',
        unsafe_allow_html=True
    )

    goal = st.radio(
        "What are you trying to achieve?",
        [
            "Maintain Weight",
            "Lose Weight",
            "Gain Weight"
        ],
        horizontal=True
    )

    calculate = st.button(
        "🔥 Calculate My Daily Calories"
    )

# ---------------------------------------------------------
# CALCULATION
# ---------------------------------------------------------
if calculate:

    # Mifflin-St Jeor equation
    if gender == "Male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    activity_factors = {
        "Sedentary — little or no exercise": 1.2,
        "Lightly Active — exercise 1–3 days/week": 1.375,
        "Moderately Active — exercise 3–5 days/week": 1.55,
        "Very Active — exercise 6–7 days/week": 1.725,
        "Extra Active — intense training / physical job": 1.9
    }

    tdee = bmr * activity_factors[activity]

    if goal == "Maintain Weight":
        target_calories = tdee
        interpretation = (
            "This is an estimated maintenance level. "
            "Eating around this amount may help you maintain your current weight."
        )

    elif goal == "Lose Weight":
        target_calories = tdee - 500
        interpretation = (
            "A moderate calorie deficit can support gradual weight loss. "
            "Focus on protein-rich foods, vegetables, whole grains and consistent activity."
        )

    else:
        target_calories = tdee + 300
        interpretation = (
            "A moderate calorie surplus can support gradual weight gain. "
            "Combine nutritious calorie-dense foods with strength training."
        )

    # Safety floor for this simple calculator
    target_calories = max(target_calories, 1200)

    st.session_state.calculated = True
    st.session_state.bmr = bmr
    st.session_state.tdee = tdee
    st.session_state.target = target_calories
    st.session_state.interpretation = interpretation

# ---------------------------------------------------------
# RESULT SECTION
# ---------------------------------------------------------
with right:

    st.markdown(
        '<div class="section-title">📊 Your Calorie Dashboard</div>',
        unsafe_allow_html=True
    )

    if st.session_state.calculated:

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-label">Recommended Daily Target</div>
                <div class="result-number">
                    {st.session_state.target:,.0f}
                </div>
                <div class="result-unit">calories / day</div>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        r1, r2 = st.columns(2)

        with r1:
            st.metric(
                "🔥 BMR",
                f"{st.session_state.bmr:,.0f} kcal"
            )

        with r2:
            st.metric(
                "⚡ TDEE",
                f"{st.session_state.tdee:,.0f} kcal"
            )

        st.markdown(
            f"""
            <div class="info-card">
                <b>💡 What does this mean?</b><br><br>
                {st.session_state.interpretation}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown(
            """
            <div class="tip-card">
                <b>🥗 Smart Tip</b><br><br>
                Calorie needs are estimates, not exact prescriptions.
                Your actual needs can vary depending on metabolism,
                body composition, exercise and daily routine.
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.info(
            "👈 Enter your details and click **Calculate My Daily Calories** "
            "to see your personalized estimate."
        )

        st.markdown(
            """
            ### 📌 How it works

            **1. Personal Details**  
            Enter your age, height, weight and gender.

            **2. Activity Level**  
            Tell us how active you are during a normal week.

            **3. Goal**  
            Choose whether you want to maintain, lose or gain weight.

            **4. Get Your Estimate**  
            CalorieFit calculates an estimated daily calorie target.
            """
        )

# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.divider()

st.caption(
    "⚠️ This calculator provides an estimate for educational purposes. "
    "Individual calorie needs can vary significantly."
)