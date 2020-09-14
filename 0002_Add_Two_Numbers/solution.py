# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ListNode(0)
        l = temp
        carry = 0
        while l1 or l2:
            val1, l1 = (l1.val, l1.next) if l1 else (0, None)
            val2, l2 = (l2.val, l2.next) if l2 else (0, None)
            l.next = ListNode((carry + val1 + val2) % 10)
            l = l.next
            carry = (carry + val1 + val2) // 10
        if carry > 0:
            l.next = ListNode(carry)
        return l.next
