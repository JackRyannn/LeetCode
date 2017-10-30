# 回文链表其实不好实现，不如转成数组再做，效率更高也更易读
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        l = []
        while head:
            l.append(head.val)
            head = head.next
        l2 = l[::-1]
        for i in range(len(l)):
            if l[i] != l2[i]:
                return False
        return True
