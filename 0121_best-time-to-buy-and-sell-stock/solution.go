package _121_best_time_to_buy_and_sell_stock

import "math"

// 1次遍历，记录最低的值，同时利用最低的值找到最大的差值，就是最大的利润
// 时间复杂度：O(n)，只需要遍历一次。
// 空间复杂度：O(1)，只使用了常数个变量。
func maxProfit(prices []int) int {
	minValue := math.MaxInt64
	maxValue := 0
	for i := 0; i < len(prices); i++ {
		if prices[i] < minValue {
			minValue = prices[i]
		} else if prices[i]-minValue > maxValue {
			maxValue = prices[i] - minValue
		}
	}
	return maxValue
}

