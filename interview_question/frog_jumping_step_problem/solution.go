package main

func numWays(n int) int {
	// 由于 dp 列表第 ii 项只与第 i-1 和第 i-2 项有关，因此只需要初始化三个整形变量 sum, a, b ，利用辅助变量 sum 使 a, b两数字交替前进即可 （具体实现见代码） 。
	//因为节省了 dp 列表空间，因此空间复杂度降至 O(1) 。

	a, b := 1, 1 //a ,b 分别是n为0和1时的跳法
	for i := 2; i <= n; i++ {
		a, b = b, (a+b)%1000000007
	}
	return b
}
