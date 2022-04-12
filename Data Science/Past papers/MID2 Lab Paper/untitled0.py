
import pandas as pd
import numpy as np
df = pd.DataFrame({'a': [0, -1, 2], 'b': [-3, 2, 1]})
print(df)

df[df['b'] < 0] = np.NaN
print(df)