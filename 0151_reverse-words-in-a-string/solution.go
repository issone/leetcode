package _151_reverse_words_in_a_string

func reverseWords(s string) string {
	if s == "" {
		return ""
	}
	res := []byte{}
	queue := []string{}

	word := []byte{}
	for i := 0; i < len(s); i++ {
		if s[i] == ' ' {
			if len(word) > 0 {
				queue = append(queue, string(word))
				word = []byte{}
			}
		} else {
			word = append(word, s[i])
		}
	}
	if len(word) > 0 {
		queue = append(queue, string(word))
	}

	if len(queue) <= 0 {
		return ""
	}

	for i := len(queue) - 1; i >= 0; i-- {
		res = append(res, []byte(queue[i])...)
		res = append(res, ' ')
	}

	return string(res[:len(res)-1])
}
