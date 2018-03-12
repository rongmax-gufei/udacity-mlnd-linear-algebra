"""
创建n*n单位矩阵
"""
class UnitMatrix(object):

    def create_unit_matrix(n):

        unit_matrix = []
        for i in range(n):
            cell = [0 if i != j else 1 for j in range(n)]
            unit_matrix.append(cell)

        ret = ""
        for k in unit_matrix:
            # 第一行
            if k == unit_matrix[0]:
                ret += "{},\n".format(k)
            # 中间行
            elif k != unit_matrix[-1]:
                ret += " {},\n".format(k)
            # 最后一行
            else:
                ret += " {}".format(k)
        return """[{}]""".format(ret)

    print(create_unit_matrix(4))