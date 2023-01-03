<h1 align="center">
  <br>
  <a href="https://www.breastcancer.org/es/"><img src="https://www.news-medical.net/image.axd?picture=2017%2F2%2Fshutterstock_576066646.jpg" alt="Breast Cancer Official Logo" width="200"></a>
  <br>
  Breast Cancer Prediction
  <br>
</h1>

<h4 align="center">Machine Learning classifier API build with FastAPI and Google cloud. This model predict whether a given patient has or not a malignant mass diagnosis. Prediction is based on patient`s clinical data. 
</h4>

<p align="center"> <a href='https://fastapi.tiangolo.com/' target="_blank"><img alt='fastapi' src='https://img.shields.io/badge/FastAPI-100000?style=for-the-badge&logo=fastapi&logoColor=009889&labelColor=FFFFFF&color=009889'/></a> <a href='https://cloud.google.com' target="_blank"><img alt='google-cloud' src='https://img.shields.io/badge/google_cloud-100000?style=for-the-badge&logo=google-cloud&logoColor=4285f4&labelColor=FFFFFF&color=4285f4'/></a> <a href='https://www.docker.com/' target="_blank"><img alt='docker' src='https://img.shields.io/badge/docker-100000?style=for-the-badge&logo=docker&logoColor=218bea&labelColor=FFFFFF&color=FFFFFF'/></a> <a href='https://dvc.org/' target="_blank"><img alt='dvc' src='https://img.shields.io/badge/dvc-100000?style=for-the-badge&logo=dvc&logoColor=19aac1&labelColor=8153bb&color=f26740'/></a>
<a href='https://scikit-learn.org/' target="_blank"><img alt='scikit-learn' src='https://img.shields.io/badge/Scikit_Learn-100000?style=for-the-badge&logo=scikit-learn&logoColor=FFFFFF&labelColor=FF4400&color=0563FF'/></a> <a href='https://www.kaggle.com/' target="_blank"><img alt='kaggle' src='https://img.shields.io/badge/Kaggle-100000?style=for-the-badge&logo=kaggle&logoColor=37BAE8&labelColor=BEFDFF&color=37BAE8'/></a> <a href='https://pandas.pydata.org/' target="_blank"><img alt='pandas' src='https://img.shields.io/badge/pandas-100000?style=for-the-badge&logo=pandas&logoColor=2D0090&labelColor=9D7BEA&color=D2C0FA'/></a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a> 
</p>

![screenshot](https://github.com/santiagoahl/breast-cancer-prediction/blob/main/introduction.gif?raw=true)

## Key Features

This machine learning model predicts the diagnosis of a patient. Prediction choses between **Malignant** and **Benign** *diagnosted* masses. The dataset is taken from the [Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data). So here are the key features of this project:

* The model is supported under a backend API built with `FastAPI` through the `POST` method, it asks the patients data as `JSON` format and returns its predicted diagnostic in the same format.

* The dataset and the current model is tracked using a `GCP` (Google Cloud) bucket.

* MLOps is done thanks to `DVC` data version control. Which helps us to connect the data and model with GCP, as well to update the model through a training pipeline in order to make an optimal CI/CD.

* The `Dockerfile` saves all required information to run the model in another machines through a container. Just running the `initializer.sh` is enough to turn the whole system on.

* The `src` dir contains all the scripts required to update the model parameters. This is done using a data preparation and a training pipeline (As previously said).

* A testing pipeline is also implemented in such a way every time that the model is updated, must pass a test to make sure that It is running without bugs.

* Attribute Information:

	* `ID number`
	* `Diagnosis` (M = malignant, B = benign)

* Ten real-valued features are computed for each cell nucleus:

	* `radius` (mean of distances from center to points on the perimeter)
	* `texture` (standard deviation of gray-scale values)
	* `perimeter`
	* `area`
	* `smoothness` (local variation in radius lengths)
	* `compactness` (perimeter^2 / area - 1.0)
	* `concavity` (severity of concave portions of the contour)
	* `concave points` (number of concave portions of the contour)
	* `symmetry`
	* `fractal dimension` ("coastline approximation" - 1)

* Dataset balancing with `imblearn.under_sampling.RandomUnderSampler`.

* Based on **Scikit-Learn** modules and functions such like:
  - `linear_model.LogisticRegression` :   Classification model.
  - `model_selection.GridSearchCV` :   Hyperparameter optimization.

* The model got a **96.3%** of f1 score and a **96.5%** of accuracy.
* The confusion matrix is the following:

<a align="center" href="https://en.wikipedia.org/wiki/Confusion_matrix"><img src="https://github.com/santiagoahl/breast-cancer-prediction/blob/main/images/confusion_matrix.png?raw=true" alt="Confusion matrix" width="400"></a>

* Our model is very sensible: **There are a few of false negatives**, which is a great result.

* Currently, the project is on **Front-End** phase. It is planned to be developed using the framework `Angular CLI`, which helps us to consume the REST API. The source code can be viewed in the directory `/static`. Here's how it looks

![screenshot](https://github.com/santiagoahl/breast-cancer-prediction/blob/main/images/website.gif)

## How To Use

To clone and run this application, follow these steps

```bash
# Clone this repository
$ git clone https://github.com/santiagoahl/breast-cancer-prediction.git

# Go into the repository
$ cd breast-cancer-prediction

# Install requirements

$ pip install -r requirements.txt
$ pip install -r requirements_test.txt
$ pip install -r api/requirements.txt

# Install Backend dependencies

$ pip install uvicorn
$ pip install fastapi

# Run the server

$ uvicorn api.main:app

# Server is set to be constant, so run in your browser:

http://127.0.0.1:8000 

# Click on `POST` method

# Click on `Try it out`

# Replace the `Request Body` with a patient data, it must have a json format, here is an example:

{
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
}

# Click on execute and view (Or download) the results

```

## Credits

This software uses the following data and packages:

- [Breast Cancer Dataset](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)
- [FastAPI](https://fastapi.tiangolo.com)
- [GCP](https://cloud.google.com)
- [Docker](https://www.docker.com)
- [Scikit-Learn](https://scikit-learn.org/stable/)
- [DVC](https://dvc.org)
- [Joblib](https://joblib.readthedocs.io/en/latest/)


## License

MIT

---

> Web Site [santiagoal.super.site](https://santiagoal.super.site/) &nbsp;&middot;&nbsp;
> GitHub [@santiagoahl](https://github.com/santiagoahl) &nbsp;&middot;&nbsp;
> Twitter [@sahumadaloz](https://twitter.com/sahumadaloz)
