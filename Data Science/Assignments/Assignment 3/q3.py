
import pandas as pd 
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import model_selection


weightage=[]
bagpercent=[]

#read data from file ad.data
readData=pd.read_csv("ad.data",header=None)

#Create label Encoder
labelEncoder=LabelEncoder()

#fit readData of 1558 using labelEncoder
readData[1558]=labelEncoder.fit_transform(readData[1558])


#converts column data into numeric type
for column in readData.columns:
    readData[column]=pd.to_numeric(readData[column], errors='coerce')
    
#fill null values with numeric
readData=readData.fillna(0)

#readData drop labels
x=readData.drop(labels=[1558],axis=1)

#readData set values on y
y=readData[1558].values

#Train, Test data, Train_size =30%, RandomState=20
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=20)


#Applying K fold
kFold=model_selection.KFold(n_splits=10,random_state=7)


#Applyting Decision Tree Classifier
#insert estimator into bagpercent, and apply BaggingClassifier
#In Q4 we have to apply AdaBoostClassifier
#calculate results and add it to its weigthage
Dt=DecisionTreeClassifier()
for i in [10,20,30,40,50,60,70,80,90,100]:
    bagpercent.append(i)
    bg=BaggingClassifier(base_estimator=Dt, n_estimators=i, random_state=7)
    results = model_selection.cross_val_score(bg,x,y, cv=kFold)
    weightage.append(results.mean())

#plot results with respect to its estimator value  
plt.plot(bagpercent,weightage)
#plot show
plt.show