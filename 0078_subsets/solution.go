package _078_subsets

// https://leetcode-cn.com/problems/subsets/solution/zi-ji-by-leetcode-solution/

//时间复杂度：O(n×2n)。一共 2^n个状态，每种状态需要 O(n)的时间来构造子集。
//空间复杂度：O(n)。即构造子集使用的临时数组 t 的空间代价
//假设nums=[1,2,3,4]，二进制的0可以写成0000，代表一个数也不取，1=0001表示去第一个数也就是[1]，
// 2=0010，表示取第二个数[2]，3=0011表示取1和2位[1,2]，4=0100表示[3]....15=1111表示[1,2,3,4]


func subsets(nums []int) (ans [][]int) {
	n := len(nums)
	// mask < 1<<n 即 mask < 2的n次方
	for mask := 0; mask < 1<<n; mask++ {
		set := []int{}
		for i, v := range nums {
			// mask二进制的第i+1位（从右到左）是否为1
			if mask&(1<<i) > 0 {
				set = append(set, v)
			}
		}
		// 因为这个set是一个局部变量，append函数在调用时是把set的指针直接赋值添加到ans后面，所以导致后面再修改set的时候会把前面的set也一同修改，
		// 所以要新建一个空值的slice，然后相当于把set的每个元素复制过去
		ans = append(ans, append([]int(nil), set...))
	}
	return
}

//https://leetcode-cn.com/problems/subsets/solution/shou-hua-tu-jie-zi-ji-hui-su-fa-xiang-jie-wei-yun-/

func subsets1(nums []int) [][]int {
	res := [][]int{}

	var dfs func(i int, list []int)
	dfs = func(i int, list []int) {
		tmp := make([]int, len(list))
		copy(tmp, list)
		res = append(res, tmp)
		for j := i; j < len(nums); j++ {
			list = append(list, nums[j])
			dfs(j+1, list)
			list = list[:len(list)-1]
		}
	}

	dfs(0, []int{})
	return res
}


