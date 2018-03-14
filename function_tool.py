
# TODO 返回矩阵的行数和列数
def shape(M):
    return (len(M), len(M[0]))


# TODO 每个元素四舍五入到特定小数数位
# 直接修改参数矩阵，无返回值
def matxRound(M, decPts=4):
    # 使用shape函数，取出行列数量
    row_count, col_count = shape(M)
    # 遍历每一行
    for row in range(row_count):
        # 遍历每一列
        for col in range(col_count):
            # 使用round函数计算后再重新赋值
            M[row][col] = round(M[row][col], decPts)
    pass


# TODO 构造增广矩阵，假设A，b行数相同
def augmentMatrix(A, b):
    # 初始化一个len(b) * len(b[0] 每项为0的数组
    result = [[0] * shape(b)[1] for i in range(shape(b)[0])]
    for i in range(len(A)):
        result[i] = A[i] + b[i]
    return result


# TODO 计算矩阵的转置
def transpose(M):
    # 利用 * 号操作符，可以将元组解压为列表
    # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    # list() 方法用于将元组转换为列表。
    return list(map(list, zip(*M)))


# TODO 计算矩阵乘法 AB，如果无法相乘则raise ValueError
def matxMultiply(A, B):
    # 使用shape函数，取出A B矩阵的行列数量
    matx_a_row_num, matx_a_clo_num = shape(A)
    matx_b_row_num, matx_b_clo_num = shape(B)

    # 先判断矩阵的相乘条件，不满足就抛出异常结束计算
    if matx_a_clo_num != matx_b_row_num:
        raise ValueError

    # 初始化一个new_matx_row_num * new_matx_col_num每项为0的数组
    new_matx_col_num = matx_b_clo_num
    new_matx_row_num = matx_a_row_num
    result = [[0] * new_matx_col_num for i in range(new_matx_row_num)]

    # 逐行遍历矩阵a
    for a_row in range(matx_a_row_num):
        # 逐列遍历矩阵b
        for b_col in range(matx_b_clo_num):
            # 取出矩阵b每行上的元素
            for b_row in range(matx_b_row_num):
                result[a_row][b_col] += A[a_row][b_row] * B[b_row][b_col]
    return result


# TODO 构造增广矩阵，假设A，b行数相同
def augmentMatrix(A, b):
    # 初始化一个len(b) * len(b[0] 每项为0的数组
    result = [[0] * shape(b)[1] for i in range(shape(b)[0])]
    for i in range(len(A)):
        result[i] = A[i] + b[i]
    return result


# TODO r1 <---> r2
# 直接修改参数矩阵，无返回值
def swapRows(M, r1, r2):
    M[r1], M[r2] = M[r2], M[r1]
    pass


# TODO r1 <--- r1 * scale
# scale为0是非法输入，要求 raise ValueError
# 直接修改参数矩阵，无返回值
def scaleRow(M, r, scale):
    if not scale:
        raise ValueError('scale can not be zero')
    else:
        M[r] = [scale * i for i in M[r]]
    pass


# TODO r1 <--- r1 + r2*scale
# 直接修改参数矩阵，无返回值
def addScaledRow(M, r1, r2, scale):
    if not scale:
        raise ValueError('scale can not be zero')
    else:
        # zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
        M[r1] = [x + (y * scale) for x, y in zip(M[r1], M[r2])]
    pass