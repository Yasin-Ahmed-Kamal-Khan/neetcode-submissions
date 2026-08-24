# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = [(root, 1)]

        longest = 0
        while len(stack) > 0:
            cur, height = stack.pop()

            if cur is not None:
                longest = max(longest, height)

                stack.append((cur.left, height + 1))
                stack.append((cur.right, height + 1))

        return longest
