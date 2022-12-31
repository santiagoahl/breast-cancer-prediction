import matplotlib.pyplot as plt
import seaborn as sns

import pandas as pd

from sklearn.pipeline import Pipeline
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from joblib import dump

def update_model(model: Pipeline) -> None:
    """
        Updates the ML model
    """
    dump(model, "models/model.pkl")

def save_simple_metrics_report(train_score: float, test_score: float, validation_score: float, model: Pipeline) -> None:
    """
        Saves the model performance report
    """
    
    with open('report.txt', 'w') as report_file:
        report_file.write('# Model Pipeline Description \n')

        for key, value in model.named_steps.items():
            report_file.write(f'### {key}: {value.__repr__} \n')

        report_file.write(f'### Train Score: {train_score} \n')
        report_file.write(f'### Test Score: {test_score} \n')
        report_file.write(f'### Validation F1 Score: {validation_score}\n')


def plot_model_performance(y_pred, y_test):
    """
        Plots the model performance
    """
    cm = confusion_matrix(y_pred, y_test)
    disp = ConfusionMatrixDisplay(cm, display_labels=['Benign', 'Malign'])
    plt.suptitle('Confusion Matrix')
    disp.plot()
    plt.show()
    plt.savefig('images/confusion_matrix.png')
 
