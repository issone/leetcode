package _167_two_sum_ii_input_array_is_sorted

/*
双指针
时间复杂度：O(n)，其中 nn 是数组的长度。两个指针移动的总次数最多为 n 次。
空间复杂度：O(1)。
初始时两个指针分别指向第一个元素位置和最后一个元素的位置。
每次计算两个指针指向的两个元素之和，并和目标值比较。
如果两个元素之和等于目标值，则发现了唯一解。
如果两个元素之和小于目标值，则将左侧指针右移一位。
如果两个元素之和大于目标值，则将右侧指针左移一位。
移动指针之后，重复上述操作，直到找到答案
*/
func twoSum(numbers []int, target int) []int {
    low, high := 0, len(numbers) - 1
    for low < high {
        sum := numbers[low] + numbers[high]
        if sum == target {
            return []int{low + 1, high + 1}
        } else if sum < target {
            low++
        } else {
            high--
        }
    }
    return []int{-1, -1}
}

