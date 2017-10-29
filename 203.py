# 删除链表中某个元素
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return
        while head.val == val:
            if head.next:
                head = head.next
            else:
                return
        node = head
        while node.next:
            if node.next.val == val:
                if node.next.next:
                    node.next = node.next.next
                else:
                    node.next = None
                continue
            node = node.next
        return head
