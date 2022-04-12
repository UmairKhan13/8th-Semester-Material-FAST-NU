"""
Created on Sun Mar 31 10:53:35 2019

@author: abdulmunimkhan
"""

import pandas as pd
import numpy as np

data = {'cities' : ['lahore','karachi',], 'provinces' : ['punjab','sindh']}
dataframe = pd.DataFrame(data)
#print(dataframe)
df1 = pd.read_json("data.json")
#print(df1.head())

df2 = pd.concat([df1, dataframe], ignore_index=True)
print(df2, "\n\n")

df3 = df2.drop_duplicates(keep='first')
print(df3, "\n\n\n")

df4 = df3.sort_values(by='provinces', ascending=True)
print("df4: \n" , df4)

df4.reset_index(drop = True, inplace = True)
print("df4: \n" , df4)