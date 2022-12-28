from utils import update_model, save_simple_metrics_report, plot_model_performance

from dvc import api

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_validate, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import f1_score, accuracy_score

import logging
from io import StringIO
import sys

import warnings

warnings.filterwarnings('ignore')

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(name)s: %(message)s',
    level=logging.INFO,
    datefmt='%H:%M:%S',
    stream=sys.stderr
)

logger = logging.getLogger(__name__)

logger.info('Loading Data ...')

data_path = api.read('data/data.csv', remote='data-track') # DVC associated paths

df = pd.read_csv(StringIO(data_path))
df.drop('id', axis=1, inplace=True)

try:
    df.drop('Unnamed: 32', axis=1, inplace=True)
except:
    pass

sc = MinMaxScaler()
X = df.drop('diagnosis', axis=1)
y = df.diagnosis

logger.info('Spliting data into train and test ...')

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


logger.info('Scaling the data ...')
X_train = pd.DataFrame(sc.fit_transform(X_train), columns=X.columns)
X_test = pd.DataFrame(sc.transform(X_test), columns=X.columns)

logger.info('Loading model ...')

column_transformer = ColumnTransformer([
    ("scaler", sc, X.columns.tolist()) # adjusts data to the same scale
], remainder="passthrough")

model = Pipeline([
    ('datafeed', column_transformer),              # grabs finalized datasets
    ('selector', SelectKBest(f_classif, k='all')), # variable selection procedure
    ('classifier', LogisticRegression(penalty='l2', C=0.5, verbose=1, n_jobs=-1))           # Logistic modeling
])

logger.info('Setting Hyperparameters to tune')

param_grid = {'classifier__multi_class':['ovr', 'multinomial'], 
              'classifier__solver': ['liblinear', 'lbfgs']
             }  
  
grid = GridSearchCV(model, param_grid, verbose = 3, cv=10, scoring=f1_score)

logger.info('Training the model ...')
# Fitting the model

grid.fit(X_train, y_train)

logger.info('Chosing the best model with CV ...')

best_model = grid.best_estimator_
y_pred = best_model.predict(X_test)
# Cross validation testing

logger.info('Computing model performance ...')

results = cross_validate(model, X, y, return_train_score=True, cv=10);
train_score = np.round(np.mean(results['train_score']), decimals=2);
test_score = np.round(np.mean(results['test_score']), decimals=2);

# F1 & Accuracy scores
model_f1_score = f1_score(y_pred, y_test, pos_label='M')
model_accuracy = accuracy_score(y_pred, y_test)


assert train_score > 0.7
assert test_score > 0.8

logger.info(f'With cross validation, The train score is {train_score} while the test score is {test_score}')
logger.info(f'The model archieved a {np.round(model_f1_score, decimals=3)*100}% of f1 score and a {np.round(model_accuracy, decimals=3)*100}% of accuracy')

logger.info('Updating model ...')
update_model(best_model)

logger.info('Generating model report ...')

validation_score = model_f1_score
save_simple_metrics_report(train_score, test_score, validation_score, best_model)

logger.info('Plotting Confusion Matrix ...')

plot_model_performance(y_pred, y_test)

logger.info('Training phase is finished.')