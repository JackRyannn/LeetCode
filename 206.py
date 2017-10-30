# 链表的反转，用三个节点即可，头一个设置为空，方便做链表结尾的空值，还有递归的方法
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        n1 = None
        while head:
            n2 = head
            head = head.next
            n2.next = n1
            n1 = n2
        return n1


