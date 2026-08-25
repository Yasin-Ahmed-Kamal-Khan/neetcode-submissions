# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def helper(self, root):
        if root is None:
            return 0, 0
        
        if root.left is None and root.right is not None:
            maxWidth, height = self.helper(root.right)
            return maxWidth, height + 1
        
        if root.right is None and root.left is not None:
            maxWidth, height = self.helper(root.left)
            return maxWidth, height + 1

        if root.right is None and root.left is None:
            return 0, 1

        maxWidthR, heightR = self.helper(root.right)
        maxWidthL, heightL = self.helper(root.left)

        maxWidth = max(maxWidthL, maxWidthR, heightL + heightR)
        maxHeight = max(heightL, heightR) + 1

        return maxWidth, maxHeight



    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        width, height = (self.helper(root))
        return max(width, height - 1)

