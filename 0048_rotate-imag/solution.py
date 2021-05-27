from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        将旋转，转换为先水平翻转，再左对角线翻转
        """
        n = len(matrix)
        # 先沿水平中线水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - 1 - i][j] = matrix[n - 1 - i][j], matrix[i][j]

        # 左对角线翻转
        for i in range(n):
            for j in range(i):  # 注意这里是i, 不是n
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
