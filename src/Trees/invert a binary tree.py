__author__ = 'Daniel'


# Given a binary tree, invert it.
# That is: swap every pair of left and right elements for each node

# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def invertBinaryTree(self,root):
        if root == None:
            return root
        else:
            temp = self.invertBinaryTree(root.left)
            root.left = self.invertBinaryTree(root.right)
            root.right = temp
            return root
