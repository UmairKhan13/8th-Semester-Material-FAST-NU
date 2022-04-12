import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score , confusion_matrix ,classification_report
from sklearn.neighbors import KNeighborsClassifier 

'''
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

'''


#importing dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv("iris.data", names=names)
print(dataset.head())
#checking numbers of observations and features in dataset
print("Shape")
print(dataset.shape)
print("Size by group")
print(dataset.groupby('class').size())

#taking vales of dataset as numpy array
array = dataset.values
print(array)
#coping all features in X
X = array[:,0:4]
#coping Target variable in Y
Y = array[:,4]


#setting train_test proportion
t_size = 0.20
#setting value of seed
seed = 7
#spliting data into train and test data with features and target values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=t_size, random_state=seed)


model=KNeighborsClassifier(n_neighbors=2)
model.fit(X_train,Y_train)
prediction=model.predict(X_test)
acc=accuracy_score(prediction,Y_test)
print(acc)

#initializing KNN classifier by default k = 5
#knn = KNeighborsClassifier() 
#knn.fit(X_train, Y_train) 
#running model on testdata
#predictions = knn.predict(X_test) 

meanAcc=0
print("KNeighborsClassifier")
for i in range(7):
    clf = KNeighborsClassifier(n_neighbors=i+1)#clf = DecisionTreeClassifier(random_state=0)
    clf.fit(X_train, Y_train )
    predictions = clf.predict(X_test)	#Predict class or regression value for X.
    acc=accuracy_score(Y_test, predictions)
    print("accuracy score at ", i , " = ", acc)
    meanAcc += acc

meanAcc=0
print("DecisionTreeClassifier")
for i in range(6):
    clf = DecisionTreeClassifier(random_state=1, max_depth=i+1)#clf = DecisionTreeClassifier(random_state=0)
    clf.fit(X_train, Y_train )
    predictions = clf.predict(X_test)	#Predict class or regression value for X.
#    print("accuracy score")
    acc=accuracy_score(Y_test, predictions)
    print("accuracy score at ", i , " = ", acc)
    meanAcc += acc
print(str(meanAcc.mean()))







'''
iris = load_iris()
cross_val_score(clf, iris.data, iris.target, cv=10)



predictions = clf.predict(X_test)	#Predict class or regression value for X.


print("confusion matrix")
print(confusion_matrix(Y_test, predictions)) 
print("classification report")
print(classification_report(Y_test, predictions))


#running model with k (k=1, 2, 3,…., 10).
for k in range(1,10):
    clf = DecisionTreeClassifier(n_neighbors= k)
    clf.fit(X_train, Y_train) 
    predictions = clf.predict(X_test) 
    print("k = {}, Accuracy = {}".format(k,accuracy_score(Y_test, predictions)))
'''