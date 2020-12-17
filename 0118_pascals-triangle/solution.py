from typing import List


class Solution:
    """
    时间复杂度：O(numRows2)。
    空间复杂度：O(1)。不考虑返回值的空间占用。
    """

    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            row = []
            for j in range(0, i + 1):
                if j == 0 or j == i:  # 每行的开头和结束都是1
                    row.append(1)
                else:  # 第n行的第i个数等于第n−1 行的第 i-1 个数和第 i 个数之和
                    row.append(ret[i - 1][j - 1] + ret[i - 1][j])
            ret.append(row)
        return ret
