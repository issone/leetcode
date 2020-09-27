class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while pre.next:
            cur = pre.next
            if cur.val == val:
                pre.next = cur.next
            else:
                pre = pre.next
        return dummy.next
