# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:19:53 2019

@author: k152897
"""

import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.cross_validation import train_test_split
from sklearn.svm import SVC

X, y = np.arange(10).reshape((5, 2)), range(5)
X
array([[0, 1],
       [2, 3],
       [4, 5],
       [6, 7],
       [8, 9]])

list(y)

X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])

cereal = pd.read_csv("wdbc.data")
print(cereal.head(5))
clf = SVC(gamma='auto')
clf.fit(X, y) 
SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,
    decision_function_shape='ovr', degree=3, gamma='auto', kernel='rbf',
    max_iter=-1, probability=False, random_state=None, shrinking=True,
    tol=0.001, verbose=False)
print(clf.predict([[-0.8, -1]]))