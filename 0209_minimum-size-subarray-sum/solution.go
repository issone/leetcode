package _209_minimum_size_subarray_sum

/*
双指针（滑动窗口）
时间复杂度：O(n)，其中 n 是数组的长度。指针start 和end 最多各移动 n 次。

空间复杂度：O(1)。


连续子数组可以表示为 [start,end]：从第 start 项到第 end 项。
当 [start,end] 子数组和 >= s，如果此时扩张窗口，条件依然满足，但背离“最小长度”的要求。
所以选择收缩窗口，start 右移，直到条件不再满足（这里是一个循环），这是在优化可行解，并让窗口长度挑战最小纪录。
当窗口的和 < s，此时应该扩张窗口，end 右移，直到条件重新满足。
总结
扩张窗口：为了找到一个可行解，找到了就不再扩张
收缩窗口：在长度上优化该可行解，直到条件被破坏
寻找下一个可行解，然后再优化到不能优化……

*/
func minSubArrayLen(s int, nums []int) int {
    n := len(nums)
    if n == 0 {
        return 0
    }
    ans := math.MaxInt32
    start, end := 0, 0
    sum := 0
    for end < n {
        sum += nums[end]
        for sum >= s {
            ans = min(ans, end - start + 1)
            sum -= nums[start]
            start++
        }
        end++
    }
    if ans == math.MaxInt32 {
        return 0
    }
    return ans
}

func min(x, y int) int {
    if x < y {
        return x
    }
    return y
}
