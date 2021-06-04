from typing import List

# https://leetcode-cn.com/problems/counting-bits/solution/bi-te-wei-ji-shu-by-leetcode-solution-0t1i/

class Solution:

    def countBits(self, n: int) -> List[int]:
        """
        时间复杂度：O(nlogn)
        空间复杂度：O(1)。除了返回的数组以外，空间复杂度为常数。
        """

        def countOnes(x: int) -> int:
            ones = 0
            while x > 0:
                x &= x - 1  # x=x&(x-1) 该运算将 x 的二进制表示的最后一个 1 变成 0, 对 x 重复该操作，直到 x 变成 0，则操作次数即为 x 的「一比特数」。
                ones += 1
            return ones

        bits = [countOnes(i) for i in range(n + 1)]
        return bits

    def countBits2(self, n: int) -> List[int]:
        """
        对于正整数 x，将其二进制表示右移一位，等价于将其二进制表示的最低位去掉，得到的数是[x/2]。如果bits[x/2] 的值已知，则可以得到bits[x] 的值：

        如果 x 是偶数，则 bits[x]=bits[x/2]；

        如果 x 是奇数，则 bits[x]=bits[x/2]+1。

        上述两种情况可以合并成：bits[x] 的值等于bits[x/2] 的值加上 x 除以 2 的余数。
        可以通过 x>>1 得到，x 除以 2 的余数可以通过 x & 1 得到，因此有：bits[x]=bits[x>>1]+(x & 1)。

        遍历从 1 到 n 的每个正整数 i，计算bits 的值。最终得到的数组 bits 即为答案。

        时间复杂度：O(n)。对于每个整数，只需要 O(1)的时间计算「一比特数」。
        空间复杂度：O(1)。除了返回的数组以外，空间复杂度为常数。
        """
        bits = [0]
        for i in range(1, n + 1):
            bits.append(bits[i >> 1] + (i & 1))
        return bits

    def countBits3(self, n: int) -> List[int]:
        """
        定义正整数 x 的「最低设置位」为 x 的二进制表示中的最低的 1 所在位。例如，10 的二进制表示是 1010(2)，其最低设置位为 2，对应的二进制表示是10(2)。
        令y=x & (x−1)，则 y 为将 x 的最低设置位从 1 变成 0 之后的数，显然0≤y<x，bits[x]=bits[y]+1。因此对任意正整数 x，都有bits[x]=bits[x & (x−1)]+1。
        遍历从 1 到 n 的每个正整数 i，计算 bits 的值。最终得到的数组bits 即为答案。

        时间复杂度：O(n)。对于每个整数，只需要 O(1)的时间计算「一比特数」。
        空间复杂度：O(1)。除了返回的数组以外，空间复杂度为常数。

        """
        bits = [0]
        for i in range(1, n + 1):
            bits.append(bits[i & (i - 1)] + 1)
        return bits
