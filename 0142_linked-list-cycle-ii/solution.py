class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        时间复杂度O(n)， 空间复杂度O(1)
        :param head:
        :return:
        """
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:  # 有环
                break
        else:  # 无环
            return None
        # fast和slow相遇时，此时slow刚入环,fast已经在环内走了n圈,将fast指向head，当fast和slow再次相遇时，slow走完一圈，fast刚入环
        fast = head
        while fast != slow:
            fast = fast.next
            slow = slow.next
        return fast
