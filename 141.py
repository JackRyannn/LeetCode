# 要判断一个单链表有没有环，要明白环的属性，指针移动永远出不去，所以只要有环，设两个步长不一样的指针往前移动，一定会相遇，否则会走到头返回False
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        p = head
        q = head
        while p and q.next and q.next.next:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False
