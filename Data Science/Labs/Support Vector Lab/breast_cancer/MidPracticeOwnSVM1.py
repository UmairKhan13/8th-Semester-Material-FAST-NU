
"""
Created on Sun Mar 31 10:08:45 2019

@author: abdulmunimkhan
"""

import pandas as pd
import numpy as np
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import KFold
from sklearn.metrics import accurarcy_score
from sklearn.cross_validation import KFold

dataset = pd.read_csv("wdbc.data", header=None)
dataset[1] = np.where(dataset[1] == 'B' , 0 , 1)
array = dataset.values
arrayCount = len(array.columns)
X = array[:, 2:arrayCount]
Y = array[:, 1]


linear = SVC(kernel='linear', C=1)
rbf = SVC(kernel='rbf', gamma=0.5)
polynomial = SVC(kernel='poly', degree=2)
gnb = GaussianNB();

kf = KFold(n_splits=10)
#kf =KFold(n=data, n_folds=10)
accSum =0
rowCount =0
for train_index, test_index in kf.split(array):
    X_train, X_test = X[train_index], X[test_index]
    Y_train, Y_test = Y[train_index], Y[test_index]
    acc = trainModel(linear, X_train, X_test, Y_train, Y_test)
    accSum = accSum+acc
    count = count + 1
    print(acc)
    
print("Avg of Linear Model: ", accSum/count)

def trainModel (model, X_train, X_test, Y_train, Y_test):
    model.fit(X_train, Y_train)
    prediction = model.predict(X_test)
    return round(accuracy_score(Y_test, prediction), 3)