package _064_minimum_path_sum

/*
创建二维数组dp，与原始网格的大小相同，dp[i][j] 表示从左上角出发到 (i,j)位置的最小路径和。显然，dp[0][0]=grid[0][0]。对于 dp 中的其余元素，通过以下状态转移方程计算元素值。
当 i>0 且 j=0 时，dp[i][0]=dp[i−1][0]+grid[i][0]。

当 i=0 且 j>0 时，dp[0][j]=dp[0][j−1]+grid[0][j]。

当 i>0 且 j>0 时，dp[i][j]=min(dp[i−1][j],dp[i][j−1])+grid[i][j]。

最后得到dp[m−1][n−1] 的值即为从网格左上角到网格右下角的最小路径和。
*/

func minPathSum(grid [][]int) int {
	rows := len(grid)
	if rows == 0 {
		return 0
	}
	columns := len(grid[0])
	if columns == 0 {
		return 0
	}
	dp := make([][]int, rows)
	for i := 0; i < len(dp); i++ {
		dp[i] = make([]int, columns)
	}
	dp[0][0] = grid[0][0]
	// 先将左侧值填充满
	for i := 1; i < rows; i++ {
		dp[i][0] = dp[i-1][0] + grid[i][0]
	}
	// 再将顶部值填充
	for j := 1; j < columns; j++ {
		dp[0][j] = dp[0][j-1] + grid[0][j]
	}

	for i := 1; i < rows; i++ {
		for j := 1; j < columns; j++ {
			dp[i][j] = getMin(dp[i-1][j], dp[i][j-1]) + grid[i][j]
		}
	}
	return dp[rows-1][columns-1]
}

func getMin(a, b int) int {
	if a < b {
		return a
	}
	return b
}
