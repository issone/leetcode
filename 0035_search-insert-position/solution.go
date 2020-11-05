package _035_search_insert_position

func searchInsert(nums []int, target int) int {
    left, right := 0, len(nums)
    for left < right {
        mid := left + (right-left) / 2  //避免left+right越界的情况
        if nums[mid] < target {
            left = mid + 1
        } else {
            right = mid
        }
    }
    return left
}

