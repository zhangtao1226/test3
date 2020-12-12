import random
import numpy as np

result = random.randint(10, 20)
res = np.random.randn(5)
ret = random.random()

print('正整数', result)  # 正整数 15
print('5个随机小数', res)  # 5个随机小数 [ 0.07352722  0.43545791 -0.46703359 -1.30487201 -1.24879296]
print('0-1随机小数', ret)  # 0-1随机小数 0.3669302649155425
