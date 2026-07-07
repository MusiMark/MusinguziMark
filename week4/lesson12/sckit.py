import pandas as pd
import numpy as np
import zipfile


df = pd.read_csv('Housing.csv')
print(df)

df = df.select_dtypes(include= np.number)
print(df)


#absolute and max

max = np.max(np.abs(df),axis=0)


scaled = df/max
print(scaled.head())


#How to open zipped folder

with zipfile.ZipFile('iris.zip') as z:
    with z.open('iris.data') as f:
        df = pd.read_csv(f, header=None)


print(df.head())
