# 在leetcode一次性做完的第一题
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA == None or headB == None:
            return
        nodeA,nodeB = headA,headB
        distA,distB = 0,0
        while nodeA:
            distA += 1
            nodeA = nodeA.next
        while nodeB:
            distB += 1
            nodeB = nodeB.next
        nodeA,nodeB = headA,headB
        if distA >= distB:
            for i in range(distA-distB):
                nodeA = nodeA.next
            while nodeA:
                if nodeA == nodeB:
                    return nodeA
                nodeA = nodeA.next
                nodeB = nodeB.next
        if distA < distB:
            for i in range(distB-distA):
                nodeB = nodeB.next
            while nodeA:
                if nodeA == nodeB:
                    return nodeA
                nodeA = nodeA.next
                nodeB = nodeB.next
        return 