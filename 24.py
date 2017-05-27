# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = head
        if not first:
            return head
        second = head.next
        if not second:
            return head
        ret = second
        h = ListNode(0)
        while second:
            first.next = second.next
            second.next = first
            h.next = second
            h = first
            if first.next:
                first = first.next
                second = first.next
            else:
                break
        return ret

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n1.next = n2
n2.next = n3
n3.next = n4
h = Solution().swapPairs(n4)
while h:
    print(h.val)
    h = h.next