# 算二叉树深度的时候，如果一边有子树，一边没有，那么只计算有的那一边，因为深度计算是根到叶，必须要到最底下的结点才可以。
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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dsf(root)
    def dsf(self,node):
        if not node:
            return 0
        if node.left == None:
            return self.dsf(node.right)+1
        if node.right == None:
            return self.dsf(node.left)+1
        return min(self.dsf(node.left),self.dsf(node.right))+1


root = Tree().makeTree([0])
Tree().deleteNullNode(root)
print Solution().minDepth(root)