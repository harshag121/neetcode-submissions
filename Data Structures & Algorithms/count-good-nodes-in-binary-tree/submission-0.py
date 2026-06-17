
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root,maxi):
            if not root:
                return 0
            good = 1 if root.val >= maxi else 0
            maxi = max(maxi,root.val)

            return (
                good 
                + dfs(root.left, maxi)
                + dfs(root.right,maxi)
            )

        return dfs(root,root.val)

        