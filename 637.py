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
    l = []
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        self.l = [[] for i in range(2000)]
        if not root:
            return []
        self.traversal(root,0)
        i = 0
        while i <len(self.l):
            if not self.l[i]:
                self.l.pop(i)
                i -= 1
            i += 1
        ll = []
        for i in self.l:
            ll.append(float(sum(i))/float(len(i)))
        return ll
    def traversal(self,node,level):
        if not self.l[level]:
            self.l[level] = []
        self.l[level].append(node.val)
        if node.left:
            self.traversal(node.left,level+1)
        if node.right:
            self.traversal(node.right,level+1)



r = Tree().makeTree([1,2,9,3,None,None,None,4,None,None,None,None,None,None,None,5])
print Solution().averageOfLevels(r)