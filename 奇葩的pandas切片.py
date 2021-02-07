import pandas as pd
import numpy as np

a = pd.DataFrame({
    'one': np.arange(10)
})
print(a)
res = a.one.iloc[1:] - a.one.iloc[:-1]
print(res)
print(a.one[1:] - a.one[:-1])
b = np.arange(10)
print(b[:-1] - b[1:])
x=a['one'].array
print(x[:-1]-x[1:])
c=a[::2]
print(c.one.array)