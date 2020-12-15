package _485_max_consecutive_ones


func findMaxConsecutiveOnes(nums []int) int {
	i, j := 0, 0    // i 代表最后一个非1的元素位置
	max := 0
	for j < len(nums) {
		if nums[j] != 1 {
			i = j + 1
		}
		j++
		if j-i > max {  // j-i代表当前连续1的个数
			max = j - i
		}
	}
	return max
}

