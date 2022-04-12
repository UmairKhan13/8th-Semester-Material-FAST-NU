#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 11:54:23 2019

@author: abdulmunimkhan
"""
import pandas as pd
import numpy as np
import math

from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold, train_test_split

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from collections import Counter



datasetTrain = pd.read_csv("german_train.csv", header=None)
datasetTest = pd.read_csv("german_test.csv", header=None)

arrayTrain = datasetTrain.values
arrayTest = datasetTest.values

arrayCount = len(datasetTrain.columns)-1

X_train = arrayTrain[:, 0:arrayCount]
Y_train = arrayTrain[:, arrayCount]
Y_train = Y_train.astype('int')


X_test = arrayTest[:, 0:arrayCount]
Y_test = arrayTest[:, arrayCount]
Y_test = Y_test.astype('int')


gnb = GaussianNB();
decisionTreeSeed1 = DecisionTreeClassifier();
decisionTreeSeed2 = DecisionTreeClassifier();
linear = SVC(kernel='linear',C=1)


# GaussianNB Accurarcy
gnb.fit(X_train,Y_train)
prediction = gnb.predict(X_test);
GaussianNBAcc = accuracy_score(Y_test,prediction)
print("Accurarcy = " , str(GaussianNBAcc))

#Decision Tree Seed 1
trainPer = 0.666
X1_train, X1_test,Y1_train, Y1_test = train_test_split(X_train, Y_train, test_size=0.33, train_size=trainPer, random_state=1)
decisionTreeSeed1.fit(X_train, Y_train)
dTS1Prediction = decisionTreeSeed1.predict(X_test)
dTS1Accuracy = accuracy_score(Y_test, dTS1Prediction)
print("Accurarcy = dTS1Accuracy" , str(dTS1Accuracy))

#Decision Tree Seed 2
trainPer = 0.666
X2_train, X2_test,Y2_train, Y2_test = train_test_split(X_train, Y_train, test_size=0.33, train_size=trainPer, random_state=2)
decisionTreeSeed2.fit(X_train, Y_train)
dTS2Prediction = decisionTreeSeed2.predict(X_test)
dTS2Accuracy = accuracy_score(Y_test, dTS2Prediction)
print("Accurarcy = dTS2Accuracy" , str(dTS2Accuracy))

#Linear
linear.fit(X_train, Y_train)
linearPredict = linear.predict(X_test)
linearAccuracy = accuracy_score(Y_test ,linearPredict)
print("linearAccuracy =  ", linearAccuracy)

predic = []
predic.append(prediction)
predic.append(dTS1Prediction)
predic.append(dTS2Prediction)
predic.append(linearPredict)

cnt = len(arrayTest)
pre_final = []
for i in range(0,cnt):
    print(i)
    xx = predic[:,i]
    pre_final.append(Counter(xx).most_common(1)[0][0])
print("Accuracy using Ensenble Classifier: "+str(round(accuracy_score(Y_test,pre_final),2)))