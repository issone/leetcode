package _136_single-number

func singleNumber(nums []int) int {
    var sum int
    for _, num := range nums{
        sum ^= num
    }
    return sum
}