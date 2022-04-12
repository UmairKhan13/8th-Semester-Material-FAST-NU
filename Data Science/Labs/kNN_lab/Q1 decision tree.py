import pandas as pd
from sklearn.datasets import load_iris
from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score , confusion_matrix ,classification_report

'''
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier

'''


#importing dataset
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv("iris.data", names=names)

#checking numbers of observations and features in dataset
print("Shape")
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
#knn = KNeighborsClassifier() 
#knn.fit(X_train, Y_train) 
#running model on testdata
#predictions = knn.predict(X_test) 
clf = DecisionTreeClassifier(random_state=0)
iris = load_iris()
cross_val_score(clf, iris.data, iris.target, cv=10)

clf.fit(X_train, Y_train )

predictions = clf.predict(X_test)	#Predict class or regression value for X.

print("accuracy score")
print(accuracy_score(Y_test, predictions))
print("confusion matrix")
print(confusion_matrix(Y_test, predictions)) 
print("classification report")
print(classification_report(Y_test, predictions))

