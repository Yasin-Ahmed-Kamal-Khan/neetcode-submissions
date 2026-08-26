# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    nodes = dict()

    def height(self, node):
        if node is None:
            return 0

        if node in self.nodes:
            return 1 + max(self.nodes[node])
        
        leftHeight = self.height(node.left)        
        rightHeight = self.height(node.right)

        self.nodes[node] = (leftHeight, rightHeight)
        return max(leftHeight, rightHeight) + 1


    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.nodes = dict()
        if root is None:
            return True

        self.height(root)

        for node in self.nodes:
            left, right = self.nodes[node]
            if abs(left - right) > 1:
                return False

        return True
            

        

        
        