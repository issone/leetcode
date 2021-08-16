from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        arr = []
        while head is not None:
            arr.append(head.val)
            head = head.next
        arr.reverse()
        return arr


