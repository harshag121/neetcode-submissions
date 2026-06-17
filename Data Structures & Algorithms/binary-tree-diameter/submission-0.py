# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.d = 0
        def getd(root):
            if not root:
                return 0
            
            l = getd(root.left)
            r = getd(root.right)

            self.d = max(self.d,l+r)
            return 1 + max(l,r)

        getd(root)

        return self.d
        