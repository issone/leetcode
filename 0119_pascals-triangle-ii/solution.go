package _119_pascals_triangle_ii

func getRow(rowIndex int) []int {
    ans := make([]int, rowIndex+1)
    ans[0] = 1
    for i := 1; i < rowIndex+1; i++ {
        for j := i; j > 0; j-- {
            ans[j] += ans[j-1]
        }
    }
    return ans
}

