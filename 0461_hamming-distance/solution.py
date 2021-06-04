# 计算 x 和 y 之间的汉明距离，可以先计算 x异或y，然后统计结果中等于 1的位数。

class Solution:
    """
    不断地检查 ss 的最低位，如果最低位为 1，那么令计数器加一，然后我们令 s 整体右移一位，这样 s 的最低位将被舍去，原本的次低位就变成了新的最低位。
    我们重复这个过程直到 s=0为止。这样计数器中就累计了 s 的二进制表示中 11的数量
    """
    def hammingDistance(self, x: int, y: int) -> int:

        s = x ^ y
        ans = 0
        while s > 0:
            ans += s & 1
            s >>= 1

        return ans
