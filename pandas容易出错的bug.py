import pandas as pd

"""
先是拼接数据，然后再根据index drop一些数据。如果拼接的时候没有忽略ignore_index，下面drop的时候就会误删很多数据
"""
a = pd.DataFrame({
    'one': [1, 2, 3],
})
b = pd.DataFrame({
    'one': [4, 5, 6]
})
c = a.append(b)
print(c)
print('======')
c.drop(c.head(2).index, inplace=True)
print(c)
