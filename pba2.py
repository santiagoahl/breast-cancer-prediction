import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.datasets import load_digits
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from sklearn.metrics import ConfusionMatrixDisplay
from matplotlib.colors import ListedColormap
  # Data manipulation
import numpy as np 
from scipy.sparse import csr_matrix
import pandas as pd 
from random import choice 

  #Data-viz 
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx 
from sklearn.tree import plot_tree

  # Scikit-Learn 
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import normalize, StandardScaler, MinMaxScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, f1_score, recall_score, accuracy_score, log_loss, average_precision_score
from imblearn.over_sampling import SMOTE

 # X-Gradient Boost
from xgboost import XGBClassifier, plot_importance

  # File handling 
import pickle
import json
import joblib
#from google.colab import drive
import warnings