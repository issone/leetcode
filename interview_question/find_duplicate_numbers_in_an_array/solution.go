package main

//题1：数组中重复的数字

//题目：在一个长度为n的数组里的所有数字都在0到n-1的范围内。
//数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
//请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。
func findRepeatNumber(nums []int) int {
	if len(nums) <= 1 {
		return -1
	}
	i := 0
	for i < len(nums) {
		if nums[i] == i {
			i++
		} else {
			if nums[nums[i]] == nums[i] {
				return nums[i]
			} else {
				nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
			}
		}
	}

	return -1

}

//func findRepeatNumber(nums []int) int {
//	if len(nums) <= 1 {
//		return -1
//	}
//	for i:= range nums {
//		for nums[i] != i {
//			if nums[nums[i]] == nums[i] {
//				return nums[i]
//			} else {
//				nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
//			}
//		}
//
//	}
//
//	return -1
//
//}

//题目2：不修改数据找出重复的数字
//在一个长度为n+1的数组里的所有数字都在1到n的范围内，所以数组中至少有一个数字是重复的
//请找出数组中任意一个重复的数字。 例如，如果输入长度为7的数组{2,3,5,4,3,2,6,7}，那么对应的输出是重复的数字2或者3。
//你设计的解决方案必须不修改数组 nums 且只用常量级 O(1) 的额外空间。
func findDuplicate(nums []int) int {
	n := len(nums)
	l, r := 1, n-1
	ans := -1
	for l <= r {
		mid := (l + r) >> 1
		cnt := 0
		for i := 0; i < n; i++ {
			if nums[i] <= mid {
				cnt++
			}
		}
		if cnt <= mid {
			l = mid + 1
		} else {
			r = mid - 1
			ans = mid
		}
	}
	return ans
}
