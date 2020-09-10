func twoSum(nums []int, target int) []int {
	m:= make(map[int] int)
	for k, v := range nums{
		if index, ok := m[v]; ok {
			return []int{index , k}
		}
		m[target-v] = k
	}
	return nil
}