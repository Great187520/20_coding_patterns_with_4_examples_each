class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            if not node:
                return 0
            left = traverse(node.left)
            right = traverse(node.right)
            if left and right:
                return 1 + min(left, right)
            if not left and not right:
                return 1
            return 1 + (left if left else right)
        return traverse(root)