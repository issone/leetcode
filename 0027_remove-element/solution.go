package _027_remove_element


func removeElement(nums []int, val int) int {
	var j = len(nums) - 1
	// 先删除队尾
	for j >= 0 && nums[j] == val {
		j--
	}

	for i := 0; i < j; i++ {
		if nums[i] == val {
			nums[i], nums[j] = nums[j], nums[i] // 将待删除的和最后一个元素交换位置
			j--
		}

		for nums[j] == val {
			j--
		}
	}

	return j + 1
}
