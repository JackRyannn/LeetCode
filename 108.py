# len／／2 就是二叉树的中间值
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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root





r = Tree().makeTree([1,2,3,4])
print Solution().sortedArrayToBST(r)