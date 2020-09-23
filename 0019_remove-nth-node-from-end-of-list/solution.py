class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        while n >= 0:  # fast先走n+1步
            """
            为什么是n+1而不是n?
            当为n时，由于遍历的终止条件是fast不为空,产生的问题就是后面slow所指向的位置就是要删除的节点，但是要删除某个节点，必须找到这个节点的前一个
            所以，让fast多走一步，这样，当fast为空时，slow指向的是待删除的节点的前一个节点
            """
            fast = fast.next
            n -= 1

        while fast:  # 这里用fast而不是fast.next 是因为fast可能为None
            fast = fast.next
            slow = slow.next
        # 此时fast到达链表尾部，slow的下一个节点即为要被删除的节点
        slow.next = slow.next.next
        return dummy.next
