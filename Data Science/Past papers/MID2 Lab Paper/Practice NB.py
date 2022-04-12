import pandas as pd
import numpy as np
import math


def test(refund,m_status,t_income):#test data is sent to this function, this will return class for the data
    t_income = int(t_income[:-1])#'K' from Taxable income is removed and converted to int
    p = {}  #this will contain class with probability, class with max prob will be returned
    for label in set(Y):    #for all labels are we are calulating probability 
        p[label] = variables_probability[label]['Refund'][refund] * variables_probability[label]['Marital Status'][m_status] * prob(variables_probability[label]['Taxable Income'][0],variables_probability[label]['Taxable Income'][1],t_income)
    class_with_max_prob = ""
    max_val=0
    for ele in p:#find class with max probability
        if p[ele]>max_val:
            class_with_max_prob = ele
            max_val = p[ele]
    return class_with_max_prob
        
def prob(mean , var , A):   #this function will return probability for continious attribute using that formula
    p = math.exp(-math.pow((A - mean),2)/(2*var))
    p *= (1/math.sqrt(2*math.pi*var))
    return p
    
#starts here
#reading tab seprated data, Tid is set as col index
df = pd.read_csv('data.txt', delimiter= '\t' , index_col = 0)

array = df.values
X = array[:,0:3]#featuress
Y = array[:,3]#labels

class_probabilities = {}#probability for class to be stored is this dict
for element in set(Y):
    class_probabilities[element] = list(Y).count(element)/len(Y)#count distinct class and div by n

#removing K from tax and turning to numeric
df['Taxable Income'] = df['Taxable Income'].astype(str).str[:-1]    
df['Taxable Income'] = pd.to_numeric(df['Taxable Income'] , errors = 'coerce')

#this dict will have prob for discrete variable and mean and variance for continious variable
variables_probability = {}

for label in set(Y):
    variables_probability[label] = {}
    for col in df.columns[:-1]:
        if not df[col].dtype == np.int64:
            #for discerte values
            variables_probability[label][col] = {}
            for val in set(df[col]):
                df1 = df[df['Evade']==label]    #this will make df for particular class
                variables_probability[label][col][val] = df1[df1[col] == val].shape[0]/df1.shape[0]#count of particular value with particular label div by total values with that label
        else:
            #for continious
            variables_probability[label][col] = []
            df1 = df[df['Evade'] ==label]
            variables_probability[label][col].append(np.mean(df1[col]))#mean
            variables_probability[label][col].append(np.var(df1[col]))#variance


print(test('No','Married','120K'))#test sample
