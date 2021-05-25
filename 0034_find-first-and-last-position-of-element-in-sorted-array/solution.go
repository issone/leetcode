package _034_find_first_and_last_position_of_element_in_sorted_array

func searchRange(nums []int, target int) []int {
	if len(nums) == 0 {
		return []int{-1, -1}
	}
	left, right := 0, len(nums)-1
	for left < right {
		mid := (right-left)/2 + left
		if nums[mid] < target {
			left = mid + 1
		} else {	// 因为要找第一个target，所以符合条件后仍需要继续往前找， 故将 num[mid]>=target的情况合并处理
			right = mid
		}
	}

	if nums[left] != target {	 // target不存在
		return []int{-1, -1}
	}
	// 此时的left是第一个target的位置，往后找最后一个target
	left2, right2 := left, len(nums)-1
	for left2 <= right2 {
		mid := (right2-left2)/2 + left2
		if nums[mid] > target {
			right2 = mid - 1
		} else {
			left2 = mid + 1
		}
	}

	//如果target存在的话，right2就是结束下标
	if right2 < left || nums[right2] != target{
		return []int{-1, -1}
	}
	return []int{left, right2}
}

