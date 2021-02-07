import numpy as np
import pandas as pd

a = pd.DataFrame({
    'one': [1, 2, 3, 4, 5]
})
a = a.drop(index=2)  # 删除第2行
# 此处删除了3这个数字，但是其它数据的index并没有发生变化
print(a)

a.reset_index(inplace=True, drop=True)  # 重置索引
print(a)
a = np.arange(1, 10)
a = np.delete(a, 4, axis=0)  # delete的是下标
print(a)
