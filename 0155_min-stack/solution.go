package _155_min_stack

import "math"

/*
与其直接在 stack 存每个值，我们存每个值与当前最小值 min 的差值 （val-min）：

push：
1). 如果当前没有任何元素，则把 min 设为当前 val
2). 同时，往 stack 放 val-min
pop：
1). 如果栈顶元素是非负数（比之前的 min 大，或相同），则直接pop栈顶元素
2). 如果栈顶元素是负数（比之前的 min 小），则当前栈顶元素就是目前的 min， pop出来之后需要更新 min = min - （栈顶数值）
top：
1). 如果栈顶元素是正数（比之前的 min 大），则 top 数值 = min + （栈顶数值）
2). 如果栈顶元素是非正数（比之前的 min 小，或相同），则当前 top 元素就等于目前的 min
getMin：
直接 return min 即可

空间复杂度O（1）

*/
type MinStack struct {
	stack []int
	min   int
	size  int
}

/** initialize your data structure here. */
func Constructor() MinStack {
	return MinStack{stack: make([]int, 0), min: math.MaxInt64}
}

func (this *MinStack) Push(x int) {
	if this.size == 0 {
		this.min = x
	}
	this.stack = append(this.stack, x-this.min) // 入栈值=原始值-最小值，小于0说明入原始值是最新的最小值
	if x < this.min {
		this.min = x
	}
	this.size ++

}

func (this *MinStack) Pop() {

	if this.stack[this.size-1] < 0 { // 入栈值=原始值-最小值，小于0说明入原始值是最新的最小值， 出栈后，最小值 = 当前最小值 - 入栈值
		this.min -= this.stack[this.size-1]
	}
	this.stack = this.stack[:this.size-1]
	this.size--
}
func (this *MinStack) Top() int {

	if this.stack[this.size-1] >= 0 {
		return this.min + this.stack[this.size-1]
	}
	// 负数时，最小值就是原始的入栈值
	return this.min
}

func (this *MinStack) GetMin() int {
	return this.min
}