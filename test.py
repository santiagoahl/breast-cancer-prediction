from fastapi.testclient import TestClient

from api.main import app

client = TestClient(app)

def test_null_predictions():
    response = client.post('/v1/prediction', json={
                                                    "radius_mean": 0,
                                                    "texture_mean": 0,
                                                    "perimeter_mean": 0,
                                                    "area_mean": 0,
                                                    "smoothness_mean": 0,
                                                    "compactness_mean": 0,
                                                    "concavity_mean": 0,
                                                    "symmetry_mean": 0,
                                                    "fractal_dimension_mean": 0,
                                                    "radius_se": 0,
                                                    "texture_se": 0,
                                                    "perimeter_se": 0,
                                                    "area_se": 0,
                                                    "smoothness_se": 0,
                                                    "compactness_se": 0,
                                                    "concavity_se": 0,
                                                    "concave_points_se": 0,
                                                    "symmetry_se": 0,
                                                    "fractal_dimension_se": 0,
                                                    "texture_worst": 0,
                                                    "smoothness_worst": 0,
                                                    "compactness_worst": 0,
                                                    "concavity_worst": 0,
                                                    "concave_points_worst": 0,
                                                    "symmetry_worst": 0,
                                                    "fractal_dimension_worst": 0
                                                    })

    assert response.status_code == 200
    assert type(response.json()['diagnostic']) is str

def test_random_prediction():
    response = client.post('/v1/prediction', json={
                                                    "radius_mean": 20.57,
                                                    "texture_mean": 17.77,
                                                    "perimeter_mean": 132.9,
                                                    "area_mean": 1326,
                                                    "smoothness_mean": 0.08474,
                                                    "compactness_mean": 0.07864,
                                                    "concavity_mean": 0.0869,
                                                    "symmetry_mean": 0.1812,
                                                    "fractal_dimension_mean": 0.05667,
                                                    "radius_se": 0.5435,
                                                    "texture_se": 0.7339,
                                                    "perimeter_se": 3.398,
                                                    "area_se": 74.08,
                                                    "smoothness_se": 0.005225,
                                                    "compactness_se": 0.01308,
                                                    "concavity_se": 0.0186,
                                                    "concave_points_se": 0.0134,
                                                    "symmetry_se": 0.01389,
                                                    "fractal_dimension_se": 0.003532,
                                                    "texture_worst": 0.1238,
                                                    "smoothness_worst": 0.1238,
                                                    "compactness_worst": 0.1866,
                                                    "concavity_worst": 0.2416,
                                                    "concave_points_worst": 0.186,
                                                    "symmetry_worst": 0.08902,
                                                    "fractal_dimension_worst": 0.08902
                                                    })
    assert response.status_code == 200
    assert type(response.json()['diagnostic']) is str
