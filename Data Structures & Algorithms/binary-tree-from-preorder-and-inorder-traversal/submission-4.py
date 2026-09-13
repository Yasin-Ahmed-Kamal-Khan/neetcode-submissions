# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        first = preorder[0]
        if preorder == []:
            return None

        stack = []

        inorder = {val: (i, TreeNode(val)) for i, val in enumerate(inorder)}
        
        for val in preorder:
            inorderIndex, node = inorder[val]

            (setAsChild, parent) = (False, None)
            while stack != []:
                topNode, topInorderIndex = stack[-1]
                if inorderIndex < topInorderIndex:
                    if not setAsChild:
                        topNode.left = node
                    else:
                        parent.right = node
                    break
                elif inorderIndex > topInorderIndex:
                    parent = topNode
                    setAsChild = True
                stack.pop()

            if setAsChild:
                parent.right = node
            stack.append((node, inorderIndex))



        return inorder[first][1]
