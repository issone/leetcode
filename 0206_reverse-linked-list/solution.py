class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        遍历法
        时间复杂度：O(n)O(n)，假设 nn 是列表的长度，时间复杂度是 O(n)O(n)。
        空间复杂度：O(1)O(1)。
        """
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        递归法
        时间复杂度：O(n)O(n)，假设 nn 是列表的长度，那么时间复杂度为 O(n)O(n)。
        空间复杂度：O(n)O(n)，由于使用递归，将会使用隐式栈空间。递归深度可能会达到 nn 层。
        """
        if head is None or head.next is None:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p