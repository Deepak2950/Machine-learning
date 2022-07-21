import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt



titanic_data = pd.read_csv('titanic/train.csv')
print(titanic_data.head())
print(titanic_data.isnull().sum())