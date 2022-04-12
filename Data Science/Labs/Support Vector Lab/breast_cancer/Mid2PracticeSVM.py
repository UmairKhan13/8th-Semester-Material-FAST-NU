#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 03:41:44 2019

@author: abdulmunimkhan
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# SVM
# week 8

import numpy as np
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
import pandas as pd
from sklearn.metrics import accuracy_score

# 
dataset = pd.read_csv("wdbc.data", header= None)
print(dataset.head())
dataset[1] = np.where(dataset[1] == 'B', 0 , 1)
ff=dataset.shape
dataset = dataset.values
features = dataset[:,2:32]
label = dataset[:,1]

def trainModel (model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    return round(accuracy_score(y_test, pred), 3)



linear = SVC(kernel='linear', C=1)
rbf = SVC(kernel='rbf', gamma=0.5)
poly = SVC(kernel='poly', degree=2)
gnb = GaussianNB()


#kf = KFold(n=ff,n_folds=10)
kf = KFold(n_splits=10)


acc=0  
count = 0
for train_index, test_index in kf.split(dataset):
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    count = count + 1
    acc1 = trainModel(linear, X_train, X_test, y_train, y_test)
    acc+=acc1;
    print("Accuracy using Fold " + str(count) + " and Linear SVM is " + str(acc1))

print("Accuracy for Linear SVM is " + str(acc/count))    
acc=0    
count = 0
for train_index, test_index in kf.split(dataset):
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    count = count + 1
    acc1 = trainModel(rbf, X_train, X_test, y_train, y_test)
    acc+=acc1;
    print("Accuracy using Fold " + str(count) + " and RBF Kernel is " + str(acc1))

print("Accuracy for RBF Kernel is " + str(acc/count))
acc=0      
count = 0
for train_index, test_index in kf.split(dataset):
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    count = count + 1
    acc1 = trainModel(gnb, X_train, X_test, y_train, y_test)
    acc+=acc1;
    print("Accuracy using Fold " + str(count) + " and Naive Bayes is " + str(acc1))    

print("Accuracy for Naive Bayes is " + str(acc/count))   
acc=0  
count = 0
for train_index, test_index in kf.split(dataset):
    X_train, X_test = features[train_index], features[test_index]
    y_train, y_test = label[train_index], label[test_index]
    count = count + 1
    acc1 = trainModel(poly, X_train, X_test, y_train, y_test)
    acc+=acc1;
    print("Accuracy using Fold " + str(count) + " and Polynomial SVM is " + str(acc1))
 
print("Accuracy for Polynomial is " + str(acc/count)) 

