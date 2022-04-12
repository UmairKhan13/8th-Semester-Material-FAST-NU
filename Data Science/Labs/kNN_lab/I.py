import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score , confusion_matrix ,classification_report ,f1_score

#importing dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv("D:\\abd\\FAST\\SEMESTER_8\\Data_Science\\Lab 4\\kNN_lab\\Iris\\iris.data", names=names)

#checking numbers of observations and features in dataset
print("Shpae")
print(dataset.shape)
print("Size by group")
print(dataset.groupby('class').size())

#taking vales of dataset as numpy array
array = dataset.values
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


#initializing KNN classifier by default k = 5
knn = KNeighborsClassifier() 
knn.fit(X_train, Y_train) 
#running model on testdata
predictions = knn.predict(X_test) 

#print(Y_test)
#print(predictions)
 
print("accuracy score")
print(accuracy_score(Y_test, predictions))
print("confusion matrix")
print(confusion_matrix(Y_test, predictions)) 
print("classification report")
print(classification_report(Y_test, predictions))
print("f1 score")
print(f1_score(Y_test, predictions,average='weighted'))


#running model with k (k=1, 2, 3,…., 10).
for k in range(1,10):
    knn = KNeighborsClassifier(n_neighbors= k)
    knn.fit(X_train, Y_train) 
    predictions = knn.predict(X_test) 
    print("k = {}, Accuracy = {}".format(k,accuracy_score(Y_test, predictions)))

#running model with seed (seed=1, 2, 3,…., 10).    
for seed in range(1,10):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=t_size, random_state=seed)
    knn = KNeighborsClassifier() 
    knn.fit(X_train, Y_train) 
    predictions = knn.predict(X_test) 
    print("seed = {}, Accuracy = {}".format(seed,accuracy_score(Y_test, predictions)))
    




