# 简单的有序链表删除重复元素
class Solution(object):
    def deleteDuplicates(self, head):
        """
      :type head: ListNode
      :rtype: ListNode
      """
        if not head:
            return
        node = head
        p = head
        while (node.next):
            node = node.next
            if p.val == node.val:
                p.next = node.next
            else:
                p = node
        return head
