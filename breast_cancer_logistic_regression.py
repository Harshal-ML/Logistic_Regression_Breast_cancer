# -*- coding: utf-8 -*-
"""Breast Cancer case study Logistic Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-ZveMHmjf9s3v5tKKC_cGQUfrWHMBtpx

## Importing the libraries
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

"""## Importing the Dataset"""

dataset = pd.read_csv('breast_cancer.csv')
x = dataset.iloc[:,1:-1].values
y = dataset.iloc[:,-1].values

"""## Spliting the dataset into train and test"""

from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test =train_test_split(x,y,test_size = 0.2, random_state=0)

"""## Feature scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

"""## Training the Logistic Classifier on training set"""

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(x_train,y_train)

"""## Predicting a New Result"""

y_pred = classifier.predict(x_test)
y_pred = y_pred.reshape(len(y_pred),1)
y_test = y_test.reshape(len(y_test),1)
np.set_printoptions (precision=2)
print(np.concatenate((y_test,y_pred),1))

"""## Confusion Matrix"""

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_pred))

"""## Accuracy score with K-fold cross validation"""

from sklearn.model_selection import cross_val_score
accuracy = cross_val_score(classifier, x,y,cv =10)
np.set_printoptions(precision = 2)
print('The mean of Cross validation is = %0.2f'% (accuracy.mean()*100))
print('The Standard deviation is = %0.2f'% (accuracy.std()*100))