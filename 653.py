class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Tree(object):
    def makeTree(self,array):
        l = []
        root = TreeNode(array[0])
        l.append(root)
        i = 1
        while i <len(array):
            new_node = TreeNode(array[i])
            l.append(new_node)
            if i % 2 == 0:
                l[(i - 1) / 2].right = new_node
            else:
                l[(i - 1) / 2].left = new_node
            i += 1
        node = root
        self.deleteNullNode(node)
        return root
    def deleteNullNode(self,node):
        if node.left:
            if node.left.val:
                self.deleteNullNode(node.left)
            else:
                node.left = None
        if node.right:
            if node.right.val:
                self.deleteNullNode(node.right)
            else:
                node.right = None



class Solution(object):
    l = set()
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.l = set()
        self.traversal(root)
        if len(self.l)<2:
            return False
        self.traversal(root)
        for i in self.l:
            if k-i in self.l - {i}:
                return True
        return False
    def traversal(self,node):
        self.l.add(node.val)
        if node.left:
            self.traversal(node.left)
        if node.right:
            self.traversal(node.right)



r = Tree().makeTree([2,None,3])
print Solution().findTarget(r)