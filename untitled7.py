# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1InQJiDKjU7NTTyqPqrtOw6SWCin0w-rv

# MLP
"""

import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data = {
    'study_hours':[2,3,4,5,6,1,7,8,2,9],
    'sleep_hours':[8,7,6,5,4,10,3,2,9,1],
    'pass':[0,0,1,1,1,0,1,1,0,1]
}
X = np.array(list(zip(data['study_hours'], data['sleep_hours'])))
y = np.array(data['pass'])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")
new_data = np.array([[4, 6], [7, 3]])
predictions = model.predict(new_data)
print(f"Predictions for new data: {predictions}")