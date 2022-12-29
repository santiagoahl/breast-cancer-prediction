from .models import PredictionRequest
from .utils import get_model, transform_to_dataframe

model = get_model()

def get_prediction(request: PredictionRequest) -> float:
    """
    Input: request. PredictionRequest instance used to compute the prediction of the model 
    Output: prediction. Prediction of the model
    """
    data_to_predict = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)[0]
    return prediction