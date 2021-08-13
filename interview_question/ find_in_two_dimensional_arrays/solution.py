from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        # 时间复杂度O（n+m）,空间复杂度O（1）
        n = len(matrix)
        if not n:
            return False
        m = len(matrix[0])
        if not m:
            return False

        # 从右上出发, 如果值小于target，则往下找（因为在右边界，所以没有往右找），大于target，则往左找（因为在上边界，所以没有往上找）
        x = m - 1
        y = 0
        while 0 <= x and y <= n - 1:
            val = matrix[y][x]
            if val == target:
                return True
            elif target < val:  # 如果大了，因为下方只会更大，说明在左方
                x -= 1
            else:  # target比val小，说明 target在当前val的右下方，由于是从最右开始，右方肯定没有了，所以往下走
                y += 1
        return False


x = [[1, 1]]

print(Solution().findNumberIn2DArray(x, 1))
