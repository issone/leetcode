package replace_spaces

// 原地修改 其实很多数组填充类的问题，都可以先预先给数组扩容带填充后的大小，然后在从后向前进行操作。
// 时间复杂度O(n),空间复杂度O(1)
func replaceSpace(s string) string {
	b := []byte(s) //	先转byte才能通过索引操作
	length := len(b)
	spaceCount := 0
	// 计算空格的数量
	for _, v := range b {
		if v == ' ' {
			spaceCount++
		}
	}
	// 空格长度为1，%20长度为3，替换1个空格，需要额外增加2个字节，故根据空格数量，扩展原有切片
	tmp := make([]byte, spaceCount*2)
	b = append(b, tmp...)

	// 从后往前遍历操作，避免从前先后填充元素 每次添加元素都要将添加元素之后的所有元素向后移动
	i := length - 1
	j := len(b) - 1
	for i >= 0 {
		if b[i] != ' ' {
			b[j] = b[i] // 不为空字符串则直接将其复制到对应位置
			j--

		} else {
			b[j] = '0'
			b[j-1] = '2'
			b[j-2] = '%'
			j -= 3
		}
		i--

	}
	return string(b)

}
