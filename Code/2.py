# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = l1.val + l2.val
        result = l1
        pl1 = l1
        l1.val = c % 10
        c //= 10
        l1, l2 = l1.next, l2.next
        while l1 and l2:
            c += l1.val + l2.val
            l1.val = c % 10
            c //= 10
            pl1 = l1
            l1, l2= l1.next, l2.next

        while l1:
            c += l1.val
            l1.val = c % 10
            pl1 = l1
            l1 = l1.next
            c //= 10

        while l2:
            c += l2.val
            pl1.next = ListNode(c % 10)
            c //= 10
            l2 = l2.next
            pl1 = pl1.next

        if c != 0:
            pl1.next = ListNode(c)

        return result