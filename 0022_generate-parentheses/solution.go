package main

import "fmt"

/*
可以分析出的结论：
当前左右括号都有大于 00 个可以使用的时候，才产生分支；
产生左分支的时候，只看当前是否还有左括号可以使用；
产生右分支的时候，还受到左分支的限制，右边剩余可以使用的括号数量一定得在严格大于左边剩余的数量的时候，才可以产生分支；
在左边和右边剩余的括号数都等于 0 的时候结算。

*/

func generateParenthesis(n int) []string {
	// 使用new方法开辟内存返回内存地址
	res := new([]string)
	backtracking(n, n, "",  res)
	//res := make([]string, 128)
	//backtracking(n, n, "",  &res)

	return *res
}

func backtracking(left, right int, tmp string, res *[]string) {
	/*
	   回溯跳出条件，
	   并不需要判断左括号是否用完，因为右括号生成的条件 right > left ，
	   所以右括号用完了就意味着左括号必定用完了
	*/
	if right == 0 {
		*res = append(*res, tmp)
		return
	}

	// 生成左括号
	if left > 0 {
		backtracking(left - 1, right, tmp + "(", res)
	}

	// 括号成对存在，有左括号才会有右括号
	if right > left {
		backtracking(left, right - 1, tmp + ")", res)
	}
}




func main() {
	fmt.Println(generateParenthesis(2))
}