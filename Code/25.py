# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or head.next is None or k <= 1:
            return head
        par2, swap1 = None, head
        child2 = head if k == 2 else head.next

        swap2, child1 = head.next, head.next.next
        par1 = head.next if k == 2 else haed

        for i in range(k-2):
            swap2 = swap2.next
            child1 = child1.next
            par1 = par1.next
        
        par1.next = swap1
        # par2.next = swap2
        swap1.next = child1
        swap2.next = child2
        swap1, swap2 = swap2, swap1
        child2 = swap1 if k == 2 else swap1.next
        par1 = swap2 if k == 2 else 
        head = swap1

        while child1:
            for i in range(k):
                if child1 is None:
                    return head
                par2, swap1, child2 = swap1, swap1.next, child2.next
                par1, swap2, child1 = par1.next, swap2.next, child1.next
            par2.next = swap2
            swap1.next = child1
            swap2.next = child2
            swap1, swap2 = swap2, swap1
        
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
data = stringToListNode('[1, 2, 3, 4, 5]')
res = sol.reverseKGroup(data, 2)
while res:
    print('%d -> ' % res.val, end='')
    res = res.next