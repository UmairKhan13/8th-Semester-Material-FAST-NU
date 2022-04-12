
import pandas as pd
import numpy as np

df1 = pd.read_csv("data1.csv", index_col=0)
df2 = pd.read_csv("data2.csv", index_col=1)

df3 = pd.concat([df1,df2], ignore_index='true')

df4 = pd.read_csv("data3.csv", index_col=0)

df5=pd.concat([df3,df4], axis=1)

df6 = pd.read_json("data.json")

df7 = pd.concat([df5,df6], ignore_index='true')

df7['A']= df7['A'].convert_objects(convert_numeric = True)
df7=df7.fillna(df7.mean())

df7.to_csv("newdata.csv")
print(df7)