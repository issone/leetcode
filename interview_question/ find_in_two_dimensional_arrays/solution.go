package main

func findNumberIn2DArray(matrix [][]int, target int) bool {
	// 时间复杂度O（nlogm）,空间复杂O（1）
	if matrix == nil {
		return false
	}
	n := len(matrix)

	if n == 0 {
		return false
	}
	m := len(matrix[0])
	if m == 0 {
		return false
	}
	//以行为单位，查看该数是否在该行范围内，在的话，执行二分查找
	for i:=0;i<n;i++ {
		// 二分之前，先判断一下范围,进一步游湖
		if matrix[i][0]<= target && matrix[i][m-1]>= target{
			ok := BinarySearch(matrix[i], target)
			if ok{
				return true
			}
		}

	}
	return false

}

func BinarySearch(li []int, val int) bool {
	l := 0
	r := len(li) - 1
	for l <= r {
		mid := l + (r-l)>>2
		if li[mid] == val {
			return true
		} else if li[mid] < val {
			l = mid + 1
		} else {
			r = mid - 1
		}
	}
	return false
}
