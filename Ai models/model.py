import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# get the data from the csv

dataset = pd.read_csv('score.csv')

# split the dataset

X = dataset[['Hours']]
y = dataset['Scores']

model = LinearRegression()

model.fit(X, y)

joblib.dump(model,'score_model.pkl')

print ('model create successfully and saved as score_model.pkl')


newModel = joblib.load('score_model.pkl')

newData = pd.DataFrame({'Hours':[9.25]})

print(newModel.predict(newData))

