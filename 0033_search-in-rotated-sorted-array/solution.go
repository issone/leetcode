package _033_search_in_rotated_sorted_array

// 数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
// 此时有序部分用二分法查找。无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.
func search(nums []int, target int) int {
    left, right := 0, len(nums)-1
    for left <= right {
        mid := (right - left) / 2 + left
        if nums[mid] == target {
            return mid
        }
        if nums[mid] >= nums[left] {    // 左边有序
            if nums[mid] > target && target >= nums[left] {
                right = mid - 1
            } else {
                left = mid + 1
            }
        } else {    // 右边有序
            if nums[mid] < target && target <= nums[right] {
                left = mid + 1
            } else {
                right = mid - 1
            }
        }
    }
    return -1
}




