# Student Exam Performance Predictor

A modern machine learning web app that predicts a student's math score based on academic and demographic input features. The app is built with Python, Streamlit, scikit-learn, and pandas.

Live Demo: https://student-number-predictor.streamlit.app/

## Overview

This project demonstrates an end-to-end machine learning workflow for regression:
- data loading and preprocessing
- feature engineering for categorical and numeric data
- model training and prediction
- deployment as an interactive Streamlit web application

## Features

- Predicts a student's math score instantly
- Accepts student details such as:
  - gender
  - race/ethnicity
  - parental level of education
  - lunch type
  - test preparation course
  - reading score
  - writing score
- Clean and user-friendly Streamlit UI
- Ready for deployment on Streamlit Cloud

## Tech Stack

- Python
- Streamlit
- pandas
- numpy
- scikit-learn
- dill

## Project Structure

```text
ML_Project/
├── artifacts/                # generated data artifacts
├── notebook/                 # EDA and training notebooks
│   └── data/stud.csv         # student dataset
├── src/
│   ├── components/           # data ingestion, transformation, model training
│   ├── pipeline/             # prediction and training pipelines
│   ├── exception.py          # custom exception handling
│   ├── logger.py             # logging utility
│   └── utils.py              # helper functions
├── streamlit_app.py          # main Streamlit app entry point
├── requirements.txt          # project dependencies
├── setup.py                  # package configuration
└── README.md                 # project documentation
```

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repository-url>
   cd ML_Project
   ```

2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate     # On macOS/Linux
   venv\Scripts\activate        # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run Locally

Start the Streamlit app with:

```bash
streamlit run streamlit_app.py
```

Then open the local URL shown in the terminal, usually:

```text
http://localhost:8501
```

## Model Details

The prediction pipeline uses:
- categorical preprocessing with one-hot encoding
- numeric preprocessing with imputation and scaling
- a regression model trained on the student dataset

## Deployment

This app is prepared for deployment on Streamlit Cloud.

### Streamlit Cloud Steps
1. Push the project to GitHub.
2. Open Streamlit Cloud.
3. Create a new app.
4. Connect your GitHub repository.
5. Set the main file to:
   ```text
   streamlit_app.py
   ```
6. Deploy the app.

## Usage

1. Open the app in your browser.
2. Enter the student's details in the form.
3. Click the prediction button.
4. View the predicted math score instantly.

## Notes

- The app is designed to be simple, interactive, and easy to use.
- It can be extended with better models, improved UI, and additional analytics in the future.

## License

This project is for educational and demonstration purposes.