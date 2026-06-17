class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            self.res.append(root.val)
            inorder(root.right)
        inorder(root)
        return self.res

        