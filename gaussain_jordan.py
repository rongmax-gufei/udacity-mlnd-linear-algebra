from helper import *
from function_tool import *

# 可逆矩阵测试数据
A1 = [[3, 5, 9],
      [-3, 4, 3],
      [7, 6, 2]]

# 奇异矩阵测试数据
A2 = [[-2, -8, -2],
      [-6, 6, 6],
      [-5, -5, 1]]

b = [[1],
     [1],
     [1]]

# 2.3.1 算法
# 步骤1 检查A，b是否行数相同
# 步骤2 构造增广矩阵Ab
# 步骤3 逐列转换Ab为化简行阶梯形矩阵 中文维基链接
# 对于Ab的每一列（最后一列除外）
#     当前列为列c
#     寻找列c中 对角线以及对角线以下所有元素（行 c~N）的绝对值的最大值
#     如果绝对值最大值为0
#         那么A为奇异矩阵，返回None (你可以在选做问题2.4中证明为什么这里A一定是奇异矩阵)
#     否则
#         使用第一个行变换，将绝对值最大值所在行交换到对角线元素所在行（行c）
#         使用第二个行变换，将列c的对角线元素缩放为1
#         多次使用第三个行变换，将列c的其他元素消为0
# 步骤4 返回Ab的最后一列
# 注： 我们并没有按照常规方法先把矩阵转化为行阶梯形矩阵，再转换为化简行阶梯形矩阵，而是一步到位。如果你熟悉常规方法的话，可以思考一下两者的等价性。
""" Gaussian Jordan 方法求解 Ax = b.
    参数
        A: 方阵 
        b: 列向量
        decPts: 四舍五入位数，默认为4
        epsilon: 判读是否为0的阈值，默认 1.0e-16
        
    返回列向量 x 使得 Ax = b 
    返回None，如果 A，b 高度不同
    返回None，如果 A 为奇异矩阵
"""
def gj_Solve(A, b, decPts=4, epsilon=1.0e-16):
    # 检查A，b是否行数相同 return None
    if len(A) != len(b): return None

    # 构造增广矩阵Ab
    matxAb = augmentMatrix(A, b)

    # 返回矩阵的行数和列数: row && column
    matxAb_row, matxAb_column = shape(matxAb)

    # # 逐列转换Ab为化简行阶梯形矩阵，对于Ab的每一列（最后一列除外）
    for c in range(matxAb_column - 1):

        max_idx, max_val = 0, 0

        for i in range(matxAb_row):
            if i < c:
                continue
            abs_current_row = abs(matxAb[i][c])
            if abs_current_row > max_val:
                max_idx = i
                max_val = abs_current_row

        # 如果绝对值最大值为0，那么A为奇异矩阵，返回None
        abs_max_val = abs(max_val)
        if abs_max_val < epsilon:
            return None
        else:
            if c != max_idx:
                swapRows(matxAb, c, max_idx)
        # 使用第二个行变换，将列c的对角线元素缩放为1
        divisor = matxAb[c][c]
        if 0 != divisor:
            scaleRow(matxAb, c, 1.0 / divisor)

        # 多次使用第三个行变换，将列c的其他元素消为0
        for i in range(matxAb_row):
            # 除去第c行，且除数不为0
            if i != c:
                # 修改参数矩阵
                scale = -matxAb[i][c]
                if abs(scale) <= epsilon:
                    continue
                addScaledRow(matxAb, i, c, scale)

    printInMatrixFormat(matxAb)

    ret = []
    for row in matxAb:
        ret.append([round(row[-1], decPts)])
    return ret

    # # 检查A，b是否行数相同 return None
    # if len(A) != len(b): return None
    #
    # # 构造增广矩阵Ab
    # matxAb = func.augmentMatrix(A, b)
    #
    # # 返回矩阵的行数和列数: row && column
    # matxAb_row, matxAb_column = func.shape(matxAb)
    #
    # # 逐列转换Ab为化简行阶梯形矩阵，对于Ab的每一列（最后一列除外）
    # for c in range(matxAb_column - 1):
    #
    #     # 矩阵行列转置，提取矩阵Ab，c列的所有元素
    #     column = func.transpose(matxAb)[c][c:]
    #
    #     # 寻找列c中 对角线以及对角线以下所有元素（行 c~N）的绝对值的最大值
    #     max_val = max(column, key=abs)
    #
    #     # 如果绝对值最大值为0，那么A为奇异矩阵，返回None
    #     abs_max_val = abs(max_val);
    #     if abs_max_val < epsilon:
    #         return None
    #
    #     # 取max_val的索引值
    #     max_val_idx = column.index(max_val) + c
    #     # 使用第一个行变换，将绝对值最大值所在行交换到对角线元素所在行（行c）
    #     func.swapRows(matxAb, c, max_val_idx)
    #
    #     # 使用第二个行变换，将列c的对角线元素缩放为1
    #     func.scaleRow(matxAb, c, 1.0/matxAb[c][c])
    #
    #     # 多次使用第三个行变换，将列c的其他元素消为0
    #     for i in range(matxAb_row):
    #         # 除去第c行，且除数不为0
    #         if i != c:
    #             # 修改参数矩阵
    #             func.addScaledRow(matxAb, i, c, -matxAb[i][c])
    #
    # ret = []
    # for row in matxAb:
    #     ret.append([round(row[-1],decPts)])
    # return ret

print(gj_Solve(A1, b))

# [-0.0421, 0.2136, 0.0065]

# 1.000,  0.000, -0.000 || -0.042
# 0.000,  1.000,  0.000 ||  0.214
# 0.000,  0.000,  1.000 ||  0.006

print(gj_Solve(A2, b))


# 参考资料：
# [Udacity P3直播课] https://m.qlchat.com/topic/details?topicId=2000000919066007
# [Python内置函数Api] http://www.runoob.com/python/python-built-in-functions.html
# [矩阵的行列获取方法] http://blog.csdn.net/luoganttcc/article/details/74080768
# [获取列表中绝对值最大值] http://zhoufeng1989.github.io/Key-parameter-in-max-min-sorted/
# [Python矩阵转置] https://baijiahao.baidu.com/s?id=1579306472315552043&wfr=spider&for=pc
# [链表推导式] https://zhidao.baidu.com/question/89558106.html
