#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 12:32:05 2019

@author: abdulmunimkhan
"""

import pandas as pd
import numpy as np
import math
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import KFold, train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from collections import Counter

#Q2 

d_train = pd.read_csv("german_train.csv",header=None)
d_test = pd.read_csv("german_test.csv",header=None)

#d_train.drop_duplicates(keep='first',inplace=True)
#d_test.drop_duplicates(keep='first',inplace=True)

arr1 = d_train.values
arr2 = d_test.values

predic = []

dd1 = (len(d_train.columns))-1
print("dd1"+str(dd1))
dd2 = (len(d_test.columns))-1

x_train= arr1[:,0:dd1]
y_train= arr1[:,dd1]
y_train = y_train.astype('int')
x_test= arr2[:,0:dd2]
y_test= arr2[:,dd2] 
y_test = y_test.astype('int')

print()
#print(y_train)
#decisiontree
test_percent=0.33
nbs = GaussianNB()
dt1 = DecisionTreeClassifier()
dt2 = DecisionTreeClassifier()
lnr = SVC(kernel='linear',C=1)

nbs.fit(x_train,y_train)
pre = nbs.predict(x_test)
predic.append(pre)
print("Accuracy score: "+str(round(accuracy_score(y_test,pre),2)))

x1_train,x1_test,y1_train,y1_test=train_test_split(x_train,y_train,train_size=0.66,test_size=test_percent,random_state=1)
dt1.fit(x1_train,y1_train)
pre = dt1.predict(x_test)
predic.append(pre)
print("Accuracy score: "+str(round(accuracy_score(y_test,pre),2)))

x1_train,x1_test,y1_train,y1_test=train_test_split(x_train,y_train,train_size=0.66,test_size=test_percent,random_state=2)
dt2.fit(x1_train,y1_train)
pre = dt2.predict(x_test)
predic.append(pre)
print("Accuracy score: "+str(round(accuracy_score(y_test,pre),2)))

lnr.fit(x_train,y_train)
pre = lnr.predict(x_test)
predic.append(pre)
print("Accuracy score: "+str(round(accuracy_score(y_test,pre),2)))


# voting
predic = np.array(predic)
cnt = len(d_test)

pre_final = []
for i in range(0,cnt):
    xx = predic[:,i]
    pre_final.append(Counter(xx).most_common(1)[0][0])
print("Accuracy using Ensenble Classifier: "+str(round(accuracy_score(y_test,pre_final),2)))