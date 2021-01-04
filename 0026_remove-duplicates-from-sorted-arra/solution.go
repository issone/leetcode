package _026_remove_duplicates_from_sorted_array


func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
	    return 0
	}
	//计数器，也充当慢指针
	count := 0
	//j为快指针
	for j:=1; j <len(nums);j++{
		if nums[count] != nums[j]{
			count++
			nums[count] = nums[j]
		}

	}
	//返回计算后的长度
	return count + 1
}

