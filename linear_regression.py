from helper import *
from function_tool import *
from gaussain_jordan import *
from matplotlib import pyplot as plt

seed = 888

m1,b1 = 4, 7

X, Y = generatePoints(seed, num=100)

## 可视化
plt.xlim((-5,5))
plt.xlabel('x',fontsize=18)
plt.ylabel('y',fontsize=18)
plt.scatter(X,Y,c='b')
plt.show()

def calculateMSE(X, Y, m, b):
    if len(X) != 0:
        return sum([(y - m * x -b) ** 2 for x, y in zip(X, Y)]) / len(X)
    else:
        raise ValueError

print(calculateMSE(X, Y, m1, b1))

# TODO 实现线性回归
'''
参数：X, Y 存储着一一对应的横坐标与纵坐标的两个一维数组
返回：m，b 浮点数
XTXh=XTY
'''
def linearRegression(X, Y):
    # 一维数组X转矩阵
    matxX = [[x, 1] for x in X]
    # 矩阵转置
    transX = transpose(matxX)
    # 矩阵相乘
    matxA = matxMultiply(transX, matxX)

    # 一维数组Y转矩阵
    matxY = [[y] for y in Y]
    # 矩阵相乘
    matxb = matxMultiply(transX, matxY)

    # 高斯消元求解
    gj_result = gj_Solve(matxA, matxb)

    # print(gj_result)

    m, b = 0.0, 0.0

    if not gj_result:
        return m, b

    gj_res_len = len(gj_result)
    if gj_res_len > 0:
        m = gj_result[0][0]
    if gj_res_len > 1:
        b = gj_result[1][0]
    return m, b


m2, b2 = linearRegression(X, Y)
assert isinstance(m2, float), "m is not a float"
assert isinstance(b2, float), "b is not a float"
print(m2, b2)
