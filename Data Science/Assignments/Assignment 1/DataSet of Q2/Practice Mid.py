#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 16:23:26 2019

@author: abdulmunimkhan
"""

import pandas as pd




df1 = pd.read_csv("data1.csv", index_col = 0);
df2 = pd.read_csv("data2.csv", index_col = 1);

print("df1: \n" , df1)
print("df2: \n" , df2)

df3 = pd.concat([df1, df2], ignore_index=True, sort=None)
print("df3: \n" , df3)

df4 = pd.read_csv("data3.csv", index_col=0);
df5 = pd.concat([df3, df4], axis=1)

print ("df5: \n" , df5);

"""
df6 = pd.read_csv("data.json", index_col = 0);
df7 = pd.concat([df5, df6], axis=1);

#pd.merge

"""
