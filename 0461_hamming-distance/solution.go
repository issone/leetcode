package _461_hamming_distance

//记 f(x)表示 x 和 x-1 进行与运算所得的结果（即 f(x)=x&(x-1)，那么 f(x) 恰为 x 删去其二进制表示中最右侧的 1 的结果。
//基于该算法，当我们计算出 s=x^y，只需要不断让 s = f(s)，直到 s=0 即可。
//这样每循环一次，s 都会删去其二进制表示中最右侧的 1，最终循环的次数即为 s 的二进制表示中 1 的数量。


func hammingDistance(x, y int) (ans int) {
	for s := x ^ y; s > 0; s &= s - 1 {
		ans++
	}
	return
}
