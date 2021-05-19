package _148_sort_list

type ListNode struct {
    Val int
    Next *ListNode
}


/*
递归版本，时间复杂度为O(nlogn),空间复杂度为 O(n)，分别由新开辟数组O(n)和递归函数调用O(logn)组成，而根据链表特性：

数组额外空间：链表可以通过修改引用来更改节点顺序，无需像数组一样开辟额外空间；
递归额外空间：递归调用函数将带来O(logn)的空间复杂度，因此若希望达到O(1)O空间复杂度，则不能使用递归。

如果fast, slow都指向头部，那么fast会走两步，slow走一步，cut点是不对的。 如果fast先走一步，就会避免长度为2时出现的特殊错误情况。当链表长度是2时，会死循环
*/
func sortList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    fast ,slow := head.Next, head

    for fast != nil && fast.Next != nil {
        fast, slow = fast.Next.Next, slow.Next
    }
    mid := slow.Next
    slow.Next =  nil
    left := sortList(head)
    right := sortList(mid)
    return mergeTwoList(left, right)


}

func mergeTwoList( left, right *ListNode) *ListNode{
    dummy := &ListNode{}
    res := dummy
    for left != nil && right != nil{
        if left.Val < right.Val{
            dummy.Next = left
            left = left.Next
        }else {
            dummy.Next = right
            right = right.Next
        }
        dummy = dummy.Next

    }
    if left != nil{
        dummy.Next = left
    }else{
        dummy.Next = right
    }
    return res.Next
}