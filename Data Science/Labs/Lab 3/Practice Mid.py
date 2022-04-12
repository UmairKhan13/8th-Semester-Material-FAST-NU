"""
Created on Sat Mar 30 16:23:26 2019

@author: abdulmunimkhan
"""

import pandas as pd
import numpy as np



df1 = pd.read_csv("data1.csv", index_col = 0);
df2 = pd.read_csv("data2.csv", index_col = 1);

print("df1: \n" , df1)
print("df2: \n" , df2)

df3 = pd.concat([df1, df2], ignore_index=True, sort=None)
print("df3: \n" , df3)

df4 = pd.read_csv("data3.csv", index_col=0);
df5 = pd.concat([df3, df4], axis=1, ignore_index=True)

print ("df5: \n" , df5);

df6 = pd.read_json("data.json")
df7 = pd.concat([df5, df6], axis = 1, ignore_index=True);
print ("df7: \n" , df7);

df8 = df7.replace(['Hello'], np.nan);
print ("df8: \n" , df8);


df9 = df8.fillna(df8.mean())
print ("df9: \n" , df9);

df9[0] = df9[0].fillna(df9.mean())
print ("df9: \n" , df9);