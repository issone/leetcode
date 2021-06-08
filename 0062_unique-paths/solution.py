class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        我们令 dp[i][j] 是到达 i, j 最多路径

        动态方程：dp[i][j] = dp[i-1][j] + dp[i][j-1]

        注意，对于第一行 dp[0][j]，或者第一列 dp[i][0]，由于都是在边界，所以只能为 1

        时间复杂度：O(m*n)

        空间复杂度：O(m*n)

        """
        dp = [[1] * n, [[1] + [0] * (n - 1) for _ in range(m - 1)]]  # 生成m行n列的二维数组，且第一行和第一列全为1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def uniquePaths2(self, m: int, n: int) -> int:
        """
        优化1：因为我们每次只需要 dp[i-1][j],dp[i][j-1]
        所以我们只要记录这两个数
        空间复杂度 O(2n)
        令m为行、n为列 优化1：行列两层循环中的循环体cur[j] = pre[j] + cur[j-1] ，cur[j] 表示遍历到的从起点到第i行第j列的路径数，
        它等于当前第i行第j-1列即 cur[j-1]的值 加上 上一行第j列的值pre[j] 内层循环一次后即计算完了第i行各列的值，
        在计算下一行第i+1行之前执行pre = cur.clone();
        即第i行的值就是第i+1行的前一行，两层循环完以后最后要到达的终点的行的值存于pre数组中，所以取出 pre[n-1]即可
        """
        pre = [1] * n   # 前一行数据
        cur = [1] * n   # 当前行数据

        for i in range(1, m):
            for j in range(1, n):
                cur[j] = pre[j] + cur[j - 1]  # 当前位置的值等于，当前行的前一列值 + 上一行的当前列的值
            pre = cur[:]  # 将当前行的数据保存到pre
        return pre[-1]

    def uniquePaths3(self, m: int, n: int) -> int:
        """
        空间复杂度 O(n)
        优化2：相比优化1，少了pre数组，cur[j] += cur[j-1]
        即 cur[j] = cur[j] + cur[j-1] 未赋值之前右边的cur[j] 始终表示当前行第i行的上一行第j列的值，赋值之后左边的cur[j]表示当前行第i行第j列的值，
        cur[j-1] 表示当前行第i行第j-1列的值(cur[j-1] 在计算cur[j]之前就已经计算了，所以表示的是当前行而不是上一行 )， 思路跟优化1是一样的，除了少用了一个数组
        """
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]
