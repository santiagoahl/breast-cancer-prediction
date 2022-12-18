<h1 align="center">
  <br>
  <a href="https://worldhappiness.report/"><img src="https://storage.googleapis.com/kaggle-datasets-images/180/384/3da2510581f9d3b902307ff8d06fe327/dataset-cover.jpg" alt="WHR" width="400"></a>
  <br>
  Breast Cancer Prediction
  <br>
</h1>

<h4 align="center">Binomial Logistic regressor built to predict whether a given patient has or not a malignant mass diagnosis. Prediction is based on patient`s clinical data. 
</h4>

<p align="center">
  <a href='https://www.kaggle.com/' target="_blank"><img alt='kaggle' src='https://img.shields.io/badge/Kaggle-100000?style=for-the-badge&logo=kaggle&logoColor=37BAE8&labelColor=BEFDFF&color=37BAE8'/></a> <a href='https://github.com/shivamkapasia0' target="_blank"><img alt='scikit-learn' src='https://img.shields.io/badge/scikit-learn-100000?style=for-the-badge&logo=scikit-learn&logoColor=FFFFFF&labelColor=FF6A00&color=1882EA'/></a> <a href='https://joblib.readthedocs.io/en/latest/' target="_blank"><img alt='joblib' src='https://img.shields.io/badge/Joblib-100000?style=for-the-badge&logo=joblib&logoColor=EA1616&labelColor=BD9B7A&color=000000'/></a>
</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a> 
</p>

![screenshot](https://static.wixstatic.com/media/260383_1358653b306a48dd9aa75142534a488d~mv2.gif)

## Key Features

This machine learning model predicts the diagnosis of a patient. Prediction choses between **Malignant** and **Benign** *diagnosted* masses. The dataset is taken from the [Breast Cancer Wisconsin (Diagnostic) Data Set](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data). So here are the key features of this project:

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

* The model got a **98.7%** of f1 score and a **98.8%** of accuracy.
* The confusion matrix is the following:

![screenshot](https://github.com/santiagoahl/breast-cancer-prediction/blob/main/images/confusion_matrix.png?raw=true)

* Our model is very sensible: **There are no false negatives** which is a great result.

## How To Use

To clone and run this application, follow these steps

```bash
# Clone this repository
$ git clone https://github.com/santiagoahl/breast-cancer-prediction.git

# Go into the repository
$ cd breast-cancer-prediction
```

## Credits

This software uses the following packages:

- [Scikit-Learn](https://scikit-learn.org/stable/)
- [Joblib](https://joblib.readthedocs.io/en/latest/)
- [Dataset](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)


## License

MIT

---

> Web Site [santiagoal.super.site](https://santiagoal.super.site/) &nbsp;&middot;&nbsp;
> GitHub [@santiagoahl](https://github.com/santiagoahl) &nbsp;&middot;&nbsp;
> Twitter [@sahumadaloz](https://twitter.com/sahumadaloz)
