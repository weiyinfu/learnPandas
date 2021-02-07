import pandas as pd

"""
DataFrame的copy会发生深复制
"""
a = pd.DataFrame({
    'one': [1, 2, 3],
    'two': [4, 5, 6],
})
b = a.iloc[1:3].copy()
b.iloc[0, 0] = 100
print(a)
