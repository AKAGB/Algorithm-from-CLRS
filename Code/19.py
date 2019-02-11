# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        k = 0
        s1 = head
        p = s2 = head
        while s1 is not None:
            if k < n:
                k += 1
            elif k == n:
                p = head
                s2 = p.next
                k += 1
            else:
                p = s2
                s2 = p.next
            s1 = s1.next
        
        # Del
        if p == s2:
            head = s2.next
        else:
            p.next = s2.next
        return head
