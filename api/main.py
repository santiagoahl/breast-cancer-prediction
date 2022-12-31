from fastapi import FastAPI
from .app.models import PredictionResponse, PredictionRequest
from .app.views import get_prediction

app = FastAPI(docs_url='/')

@app.post('/v1/prediction')
def make_model_prediction(request: PredictionRequest):
    """
    Input: Prediction request
    Output: Prediction response. The prediction is 0 for Benign samples and 1 for Malignant samples, so we return the name instead the number
    """
    return PredictionResponse(diagnostic=get_prediction(request))