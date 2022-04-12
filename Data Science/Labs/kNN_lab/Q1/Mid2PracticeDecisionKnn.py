#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 01:33:24 2019

@author: abdulmunimkhan
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv("iris.data", names=names)
print("Dataset Shape: " , dataset.shape)

array = dataset.values
columnLen = len(dataset.columns) - 1
print(columnLen)
X = array[:,0:columnLen] #0 to 3
y = array[:, columnLen]


t_set = 0.20;

for i in range(1,8):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y , 
                                                    test_size= t_set,
                                                    random_state = i);
    model = KNeighborsClassifier(n_neighbors=i)
    model.fit(X_train, Y_train)
    prediction = model.predict(X_test)
    acc = accuracy_score(prediction, Y_test)
    print(acc)
    
for l in range(6):
    model = DecisionTreeClassifier(random_state=1,max_depth = l + 1 )
    model.fit(X_train, Y_train)
    prediction = model.predict(X_test)
    acc = accuracy_score(prediction, Y_test)
    print(acc)

