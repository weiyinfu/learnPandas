import pandas as pd

a = pd.DataFrame([1, 2, 3, 4])
print(a)
a.drop(a.head(2).index, inplace=True)
print(a)

a = pd.DataFrame([1, 2, 3, 4])
a.drop(a.tail(2).index, inplace=True)
print(a)
