# 题目没说k大于list长度该怎么办，得自己错几次才知道什么要求，辣鸡题目。
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k == 0 or not head or not head.next:
            return head
        first = head
        node = head
        count = 0
        while(node):
            count += 1
            node = node.next
        k = k%count
        if k == 0:
            return head
        node = head
        i = 0
        while(i<k):
            node = node.next
            i += 1
        while(node.next):
            head = head.next
            node = node.next
        ret = head.next
        head.next = None
        node.next = first
        return ret


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n1.next = n2
n2.next = n3
# n3.next = n4
# n4.next = n5
first = Solution().rotateRight(n1,4)
while(first):
    print(first.val)
    first = first.next
