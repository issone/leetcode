package main

func combinationSum(candidates []int, target int) [][]int {
	res := [][]int{}
	end := len(candidates)
	if end == 0 {
		return res
	}
	var dfs func(start int, temp []int, tmpTarget int)
	dfs = func(start int, temp []int, tmpTarget int) {
		if tmpTarget < 0 {
			return
		}
		if tmpTarget == 0 {
			newTmp := make([]int, len(temp))
			copy(newTmp, temp)
			res = append(res, newTmp)
			return
		}
		for i := start; i < end; i++ {
			temp = append(temp, candidates[i])
			dfs(i, temp, tmpTarget-candidates[i])
			temp = temp[:len(temp)-1]
		}

	}
	dfs(0, []int{}, target)
	return res

}
