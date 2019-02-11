# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        p1 = None
        p2 = head
        p3 = p2.next
        p4 = p3.next
        head = head.next
        while p2 and p3:
            if p1:
                p1.next = p3
            p2.next = p4
            p3.next = p2
            if p4 is None or p4.next is None:
                break
            p1 = p2
            p2 = p4
            p3 = p4.next
            p4 = p3.next
        return head

def stringToIntegerList(input):
    import json
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

sol = Solution()
data = stringToListNode('[1, 2, 3, 4]')
res = sol.swapPairs(data)
while res:
    print('%d -> ' % res.val, end='')
    res = res.next