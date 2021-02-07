import pandas as pd

a = pd.DataFrame({
    'one': [1, 2, 3]
})
a.drop(1, axis=0, inplace=True)
b = pd.DataFrame({
    'one': [4, 5, 6]
})
# 拼接操作返回新的一份数据
print('=' * 10, 'a')
print(a)
print('=' * 10, 'c')
print(a.append(b, ignore_index=True))  # 忽略index会只拼接数据，然后从头创建索引
print('=' * 10, 'ignore_index=False')
"""
下面这种方式会产生重复index
"""
print(a.append(b, ignore_index=False))
d = a.append(b)
print(d.index)
print(d.loc[2])  # 返回两行数据
