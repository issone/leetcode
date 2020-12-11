package _561_array_partition_i

import "sort"

func arrayPairSum(nums []int) int {
	sort.Ints(nums)
	sum := 0
	for i := 0; i < len(nums); i++ {
		if i%2 == 0 {
			sum += nums[i]
		}
	}
	return sum
}
