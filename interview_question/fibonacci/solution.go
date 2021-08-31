package main

func fib(n int) int {
	if n == 0 || n == 1 {
		return n
	}
	res := make([]int, n+1)
	res[0] = 0
	res[1] = 1
	for i := 2; i <= n; i++ {
		res[i] = (res[i-1] + res[i-2]) % 1000000007
	}
	return res[n]
}


//func fib(n int) int {
//	a,b :=0, 1
//	for i:=0;i<n;i++{
//		a,b = b, (a+b)%1000000007
//	}
//	return a
//}