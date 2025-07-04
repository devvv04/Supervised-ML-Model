# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1x5ocJ13rQU0nXoq7aywmdpEowywq53tr
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

url =  "https://gist.githubusercontent.com/devvv04/d6a8e4735cf035ddf404c5054684ef24/raw/d4e47d0f4ad530ce0fa83d33faa195d182b52d49/temperature_humidity.csv"
data = pd.read_csv(url, delimiter='\t')
data.head()
print(data.info())

print(data.describe())
print(data.info())

sns.scatterplot(x='Temperature', y='Humidity', data=data)
plt.title('Temperature vs Humidity')
plt.xlabel('Temperature (°C)')
plt.ylabel('Humidity (%)')
plt.show()

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

X = data[["Temperature"]]
y = data["Humidity"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=34)

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Intercept: {model.intercept_}")
print(f"Coefficient: {model.coef_[0]}")

y_pred = model.predict(X_test)

df_pred = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(df_pred)

plt.scatter(X_test, y_test, color='yellow')
plt.plot(X_test, y_pred, color='blue')
plt.title('Regression Line (Test Set)')
plt.xlabel('Temperature')
plt.ylabel('Humidity')
plt.show()