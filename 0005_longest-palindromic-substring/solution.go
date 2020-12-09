package _005_longest_palindromic_substring

func longestPalindrome(s string) string {
	/*
	动态规划分析：
	如果s[i:j]是回文子串（这里是左闭右闭），则，s[i] == s[j], 且s[i+1,j-1]也一定是回文子串
	所以s[i:j]的结果是依赖s[i+1,j-1]的，我们要提前得出s[i+1,j-1]的结果
	对应二维数组，假设纵坐标为i，横坐标为j，由于i<j，所以需要计算的值都在左对角线的右上方，
	由于s[i+1,j-1]是相对于s[i:j]的左下方，所以我们为了保证先得到s[i+1,j-1]值，考虑纵向自上而下的遍历，
	即从i=0开始遍历

	以上条件，是基于s的长度大于2时考虑
	对于长度为1的子串，一定是回文子串，长度为2的，只要这两个值相等则为回文子串，及s[i]==s[i+1
	*/

	n := len(s)
	ans := ""
	dp := make([][]bool, n)
	for i := 0; i < n; i++ {
		dp[i] = make([]bool, n)
	}
	//dp[i][j]的值，表示子串[i..j]是否是回文子串
	//如果dp[i][j]为true,则表示s[i]==s[j],可继续判断d[i+1][j-1]是否是true
	// 从长度较短的字符串向长度较长的字符串进行转移的，l代表，从i开始往后数l个数作为j
	for l := 0; l < n; l++ {
		for i := 0; i+l < n; i++ {
			j := i + l
			if l == 0 {	// l=0时，就是单个元素，必为回文
				dp[i][j] = true
			} else if l == 1 {	// 即子串长度为2， 如果，这两个值相等，也一定是回文
				if s[i] == s[j] {
					dp[i][j] = true
				}
			} else {	// 子串长度大于2的情况，状态转移
				if s[i] == s[j] {
					dp[i][j] = dp[i+1][j-1]
				}
			}
			if dp[i][j] == true && l+1 > len(ans) {
				ans = s[i : i+l+1]
			}
		}
	}
	return ans

}
