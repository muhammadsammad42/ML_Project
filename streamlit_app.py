import streamlit as st
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

st.set_page_config(page_title='Student Exam Performance Predictor', page_icon='🎓', layout='wide')

st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #f8fbff 0%, #eef4ff 100%);
    }
    .hero-box {
        background: linear-gradient(135deg, #2563eb 0%, #7c3aed 100%);
        padding: 2rem 2rem 2.2rem 2rem;
        border-radius: 24px;
        box-shadow: 0 12px 30px rgba(37, 99, 235, 0.22);
        margin-bottom: 1.2rem;
        color: white;
    }
    .hero-box h1 {
        font-size: 2.1rem;
        font-weight: 700;
        margin-bottom: 0.3rem;
    }
    .hero-box p {
        font-size: 1rem;
        opacity: 0.95;
        margin-bottom: 0;
    }
    .info-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 18px;
        padding: 1rem 1.1rem;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.06);
        margin-bottom: 1rem;
    }
    .form-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 20px;
        padding: 1.2rem 1.3rem;
        box-shadow: 0 10px 30px rgba(15, 23, 42, 0.06);
    }
    .result-card {
        background: linear-gradient(135deg, #ecfeff 0%, #eff6ff 100%);
        border: 1px solid #bfdbfe;
        border-radius: 20px;
        padding: 1.2rem;
        margin-top: 1rem;
    }
    .result-score {
        font-size: 2rem;
        font-weight: 700;
        color: #1d4ed8;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="hero-box">
        <h1>Student Exam Performance Predictor</h1>
        <p>Estimate a student's math score with a modern, polished experience powered by a trained predictive model.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('<div class="info-card"><b>🎯 Goal</b><br>Predict academic performance with a simple form.</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="info-card"><b>📊 Inputs</b><br>Demographics, study profile, and exam scores.</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="info-card"><b>⚡ Result</b><br>Get a quick math score estimate instantly.</div>', unsafe_allow_html=True)

st.markdown('<div class="form-card">', unsafe_allow_html=True)
with st.form('prediction_form'):
    st.subheader('Fill in the student details')
    col_left, col_right = st.columns(2)

    with col_left:
        gender = st.selectbox('Gender', ['female', 'male'])
        race_ethnicity = st.selectbox('Race / Ethnicity', ['group A', 'group B', 'group C', 'group D', 'group E'])
        parental_level_of_education = st.selectbox(
            'Parental Education',
            ['some high school', 'high school', 'some college', "associate's degree", "bachelor's degree", "master's degree"]
        )
        lunch = st.selectbox('Lunch Type', ['standard', 'free/reduced'])
        test_preparation_course = st.selectbox('Test Preparation Course', ['none', 'completed'])

    with col_right:
        reading_score = st.number_input('Reading Score', min_value=0, max_value=100, step=1, value=75)
        writing_score = st.number_input('Writing Score', min_value=0, max_value=100, step=1, value=70)

    submitted = st.form_submit_button('Predict Math Score', use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

if submitted:
    custom_data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=int(reading_score),
        writing_score=int(writing_score)
    )

    data_df = custom_data.get_data_as_dataframe()
    predict_pipeline = PredictPipeline()
    prediction = predict_pipeline.predict(features=data_df)

    st.markdown(
        f"""
        <div class="result-card">
            <h3>Prediction Ready</h3>
            <p>Based on the information provided, the estimated math score is:</p>
            <div class="result-score">{round(prediction[0], 2)}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
