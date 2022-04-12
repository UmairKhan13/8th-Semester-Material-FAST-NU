#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 03:46:34 2019

@author: abdulmunimkhan
"""

import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold

dataset = pd.read_csv("wdbc.data", header=None)
dataset[1] = np.where(dataset[1]=='B' , 0 , 1)
print(dataset.head())

array = dataset.values
arrayLen = len(dataset.columns)
print(arrayLen)
X = array[:, 2:arrayLen]
Y = array[:, 1]

def trainModel (model, X_train, Y_train, X_test, Y_test):
    model.fit(X_train, Y_train)
    predict = model.predict(X_test);
    acc = round(accuracy_score(Y_test, predict), 3)
    return acc;

linear = SVC(kernel='linear', C=1)
rbf = SVC(kernel='poly', degree=2)
polynomial = SVC(kernel= 'rbf', gamma=0.5)
nb = GaussianNB();

kf = KFold(n_splits=20)

accSum = 0
count = 0
for train_index, test_index in kf.split(dataset):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]
    acc = trainModel(linear, X_train, Y_train, X_test, Y_test)
    count = count + 1
    accSum = accSum + acc
    print("Result of Linear Model at K",count," is ",acc)
    
print("accuracy of Linear Model is ", (accSum/count))
    
count = 0
for train_index, test_index in kf.split(dataset):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]
    acc = trainModel(rbf, X_train, Y_train, X_test, Y_test)
    count = count + 1
    print("Result of RBF Model at K",count," is ",acc)
        

count = 0
for train_index, test_index in kf.split(dataset):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]
    acc = trainModel(rbf, X_train, Y_train, X_test, Y_test)
    count = count + 1
    print("Result of Polynomial Model at K",count," is ",acc)    