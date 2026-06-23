

from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')

    custom_data = CustomData(
        gender=request.form['gender'],
        race_ethnicity=request.form['race_ethnicity'],
        parental_level_of_education=request.form['parental_level_of_education'],
        lunch=request.form['lunch'],
        test_preparation_course=request.form['test_preparation_course'],
        reading_score=int(request.form['reading_score']),
        writing_score=int(request.form['writing_score'])
    )

    # Get the data as a DataFrame
    data_df = custom_data.get_data_as_dataframe()

    # Initialize the prediction pipeline
    predict_pipeline = PredictPipeline()

    # Make the prediction
    prediction = predict_pipeline.predict(features=data_df)

    return render_template('home.html', results=round(prediction[0], 2))

if __name__ == "__main__":
    app.run(host="0.0.0.0")