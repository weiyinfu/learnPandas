import pandas as pd
import numpy as np

"""
下面代码中会发生数据拷贝，更改pandas并不会影响原数组
"""
one = [1, 2, 3]
two = np.array([4, 5, 6])
a = pd.DataFrame({
    'one': one,
    'two': two
})
print(a)
one[0] = 100
two[0] = 100
print(a)
a['one'][0] = 1342
print(one)
