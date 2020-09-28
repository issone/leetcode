package _234_palindrome_linked_list

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
    if head == nil || head.Next == nil {
        return true
    }
    fast := head
    slow := head

    for fast.Next != nil && fast.Next.Next !=nil {
        fast = fast.Next.Next
        slow = slow.Next
    }
    // 此时slow指向前半部分的尾结点, 反转后半部分的链表
    second_half_start := reverseLink(slow.Next)
    first := head
    second := second_half_start
    for  first != nil && second != nil {
        if first.Val != second.Val {
            return false
        }
        first = first.Next
        second = second.Next
    }

    return true
}


func reverseLink(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    var pre *ListNode
    var tmp *ListNode
    for head != nil {
        tmp = head.Next
        head.Next = pre
        pre = head
        head = tmp
    }
    return pre
}