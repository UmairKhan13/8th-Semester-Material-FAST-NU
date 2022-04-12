import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score , confusion_matrix ,classification_report

#importing dataset
#names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
datatraining = pd.read_csv("D:\\abd\\FAST\\SEMESTER 8\\Data Science\\Lab 4\\kNN_lab\\Iris\\datatraining.txt")
datatest = pd.read_csv("D:\\abd\\FAST\\SEMESTER 8\\Data Science\\Lab 4\\kNN_lab\\Iris\\datatest.txt")
datatest2 = pd.read_csv("D:\\abd\\FAST\\SEMESTER 8\\Data Science\\Lab 4\\kNN_lab\\Iris\\datatest2.txt")

#checking numbers of observations and features in dataset
print("Shpae of training data")
print(datatraining.shape)
print("Shpae of test data")
print(datatest.shape)
print("Shpae of test2 data")
print(datatest2.shape)

#taking vales of dataset as numpy array
array_train = datatraining.values
array_test = datatest.values
array_test2 = datatest2.values
#coping all features in X
X_train= array_train[:,1:6]
X_test = array_test[:,1:6]
X_test2 = array_test2[:,1:6]

#coping Target variable in Y
Y_train= array_train[:,6]
Y_train = Y_train.astype('int')
Y_test = array_test[:,6]
Y_test = Y_test.astype('int')
Y_test2 = array_test2[:,6]
Y_test2 = Y_test2.astype('int')

#initializing KNN classifier by default k = 5
knn = KNeighborsClassifier() 
knn.fit(X_train, Y_train)
 
print("On testdata 1")
#running model on testdata
predictions = knn.predict(X_test) 
print("\naccuracy score")
print(accuracy_score(Y_test, predictions))
print("\nconfusion matrix")
print(confusion_matrix(Y_test, predictions)) 
print("\nclassification report")
print(classification_report(Y_test, predictions))

print("On testdata 2")

#running model on testdata2
predictions2 = knn.predict(X_test2) 
print("\naccuracy score")
print(accuracy_score(Y_test2, predictions2))
print("\nconfusion matrix")
print(confusion_matrix(Y_test2, predictions2)) 
print("\nclassification report")
print(classification_report(Y_test2, predictions2))

#on testdata1
#running model with k (k=1, 2, 3,…., 10).
print("\nChecking Different K on Testdata 1")
for k in range(1,11):
    knn = KNeighborsClassifier(n_neighbors= k)
    knn.fit(X_train, Y_train) 
    predictions = knn.predict(X_test) 
    print("k = {}, Accuracy = {}".format(k,accuracy_score(Y_test, predictions)))

#on testdata2
#running model with k (k=1, 2, 3,…., 10).
print("\nChecking Different K on Testdata 2")
for k in range(1,11):
    knn = KNeighborsClassifier(n_neighbors= k)
    knn.fit(X_train, Y_train) 
    predictions2 = knn.predict(X_test2) 
    print("k = {}, Accuracy = {}".format(k,accuracy_score(Y_test2, predictions2)))





