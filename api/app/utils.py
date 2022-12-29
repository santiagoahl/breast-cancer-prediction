from joblib import load
from sklearn.pipeline import Pipeline
from pydantic import BaseModel
from pandas import DataFrame
import os
from io import BytesIO

def get_model()->Pipeline:
    """
    Input:
    Output:
    """
    model_path = os.environ.get('MODEL_PATH', 'models/model.pkl')
    with open(model_path, 'rb') as model_file:
        model = load(BytesIO(model_file.read()))
    return model

def transform_to_dataframe(class_model: BaseModel) -> DataFrame:
    """
    Input:
    Output:
    """
    dictionary = {key: [value] for key, value in class_model.dict().items()}
    df = DataFrame(dictionary)
    return df