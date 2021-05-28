package _070_climbing_stairs

func climbStairs(n int) int {
    if n == 1 || n== 2{
        return n
    }
    first , second := 1, 2
    for i:=3; i<=n;i++{ // 滚动数组

        first, second = second, first+second
    }
    return second
}
