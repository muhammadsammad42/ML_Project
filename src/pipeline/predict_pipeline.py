
import sys
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from src.exception import CustomException


class PredictPipeline:
    def __init__(self):
        self.model = None
        self.preprocessor = None
        self._build_pipeline()

    def _build_pipeline(self):
        try:
            categorical_features = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
            numeric_features = ['reading_score', 'writing_score']

            categorical_transformer = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehot', OneHotEncoder(handle_unknown='ignore'))
                ]
            )

            numeric_transformer = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            preprocessor = ColumnTransformer(
                transformers=[
                    ('cat', categorical_transformer, categorical_features),
                    ('num', numeric_transformer, numeric_features)
                ]
            )

            model = LinearRegression()

            self.preprocessor = preprocessor
            self.model = Pipeline(steps=[('preprocessor', preprocessor), ('regressor', model)])

            # Train a simple model from the local dataset for local use.
            df = pd.read_csv('notebook/data/stud.csv')
            X = df[['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course', 'reading_score', 'writing_score']]
            y = df['math_score']
            self.model.fit(X, y)

        except Exception as e:
            raise CustomException(e, sys)

    def predict(self, features):
        try:
            return self.model.predict(features)

        except Exception as e:
            raise CustomException(e, sys)
        
class CustomData:
    def __init__(self,  gender: str,
                 race_ethnicity: str,
                 parental_level_of_education: str,
                 lunch: str,
                 test_preparation_course: str,
                 reading_score: int,
                 writing_score: int):
        self.gender = gender
        self.race_ethnicity = race_ethnicity
        self.parental_level_of_education = parental_level_of_education
        self.lunch = lunch
        self.test_preparation_course = test_preparation_course
        self.reading_score = reading_score
        self.writing_score = writing_score

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],
            }

            return pd.DataFrame(custom_data_input_dict)

        except Exception as e:
            raise CustomException(e, sys)