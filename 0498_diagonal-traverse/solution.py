from typing import List


class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        1. 在一条对角线上的元素，其横纵坐标之和是一个定值
        2. 遍历每个元素，将元素分组到各对角线上
        3. 由于是从上到下，一行行遍历的，所以每个对角线 所对应的结果列表，相当于是从上往下（左下方向）入队，因此右上方向的走的数据需要翻转的结果
        """
        result = []
        group = {}
        for i, row in enumerate(matrix):
            for j, num in enumerate(row):
                group.setdefault(i + j, []).append(num)
        for k, v in group.items():
            if k % 2:
                result += v

            else:  # 右上方向需要翻转
                result += v[::-1]
        return result
