package _046_permutations

/*

为什么要回溯
我们不是找到一个排列就完事，要找出所有满足条件的排列。

递归结束时，结束的是当前的递归分支，还要去别的分支继续搜。

所以，要撤销当前的选择，回到选择前的状态，去选下一个选项，即切入下一个分支。

注意，往map添加的当前选择也要同时撤销。代表没有做这个选择。

退回来，把路走全，才能在一棵空间树中，回溯出所有的解。


为什么加入解集时，要将数组（在go中是切片）内容拷贝到一个新的数组里，再加入解集。

这个 path 变量是一个地址引用，结束当前递归，将它加入 res，后续的递归分支还要继续进行搜索，还要继续传递这个 path，这个地址引用所指向的内存空间还要继续被操作，
所以 res 中的 path 所引用的内容会被改变，这就不对，所以要拷贝一份内容，到一份新的数组里，然后放入 res，这样后续对 path 的操作，就不会影响已经放入 res 的内容。
*/

func permute(nums []int) [][]int {
	res := [][]int{}
	visited := map[int]bool{} // 记录选过的数，下次遇到相同的数，跳过

	var dfs func(path []int)
	dfs = func(path []int) {
		if len(path) == len(nums) {
			temp := make([]int, len(path))
			copy(temp, path)
			res = append(res, temp)
			return
		}
		for _, n := range nums {
			if visited[n] { // 不能重复选
				continue
			}
			path = append(path, n)
			visited[n] = true
			dfs(path)
			path = path[:len(path)-1]
			visited[n] = false
		}
	}

	dfs([]int{})
	return res
}
