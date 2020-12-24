package _557_reverse_words_in_a_string_iii
/*
开辟一个新字符串。然后从头到尾遍历原字符串，直到找到空格为止，此时找到了一个单词，并能得到单词的起止位置。
随后，根据单词的起止位置，可以将该单词逆序放到新字符串当中。
如此循环多次，直到遍历完原字符串，就能得到翻转后的结果。
时间复杂度：O(N)，其中 N 为字符串的长度。原字符串中的每个字符都会在 O(1) 的时间内放入新字符串中。

空间复杂度：O(N)。我们开辟了与原字符串等大的空间。

*/
func reverseWords(s string) string {
    length := len(s)
    ret := []byte{}
    for i := 0; i < length; {
        start := i
        // 得到一个单词
        for i < length && s[i] != ' ' {
            i++
        }

        // 将单词翻转
        for p := start; p < i; p++ {
            ret = append(ret, s[start + i - 1 - p])
        }

        // 为单词间加入空格
        for i < length && s[i] == ' ' {
            i++
            ret = append(ret, ' ')
        }
    }
    return string(ret)
}
