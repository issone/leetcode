from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        row = len(matrix)
        col = len(matrix[0])
        is_sign = False
        for i in range(row):
            if matrix[i][0] == 0:  # 标记第一列中是否有0，提前保存，防止被后面检测时，覆盖了(0，0)的值
                is_sign = True
            for j in range(1, col):  # 跳过第一列，检查其他行列是否有0
                if matrix[i][j] == 0:  # 将当前行的第一个和当前列的第一个设为0
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, row):  # 跳过第一行和第一列，检查标识位置是否出现过0
            for j in range(1, col):
                if matrix[i][0] == 0 or matrix[0][j] == 0:  # 当前行或列的第一个是0，代表此行或列出现过0
                    matrix[i][j] = 0
        if matrix[0][0] == 0:  # 第一行需要被设置为0
            for i in range(col):
                matrix[0][i] = 0

        if is_sign:  # 第一列中出现过0，所以第一列需要被设置为0
            for i in range(row):
                matrix[i][0] = 0
