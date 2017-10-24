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