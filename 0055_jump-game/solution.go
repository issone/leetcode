package _055_jump_game

func canJump(nums []int) bool {
	// 从前往后推
	reachable := 0
	for i, v := range nums {
		if i > reachable {	// 当索引位置超过最大可达的位置时，说明不可能到达
			return false
		}
		reachable = getMax(reachable, i + v)
	}
	return true


}
func getMax(a, b int) int {
	if a > b {
		return a
	}
	return b
}
