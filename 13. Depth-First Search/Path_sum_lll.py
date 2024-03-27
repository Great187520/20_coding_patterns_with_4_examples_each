class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.total = 0
        def helper(node, cur):
            if not node:
                return
            helper(node.left,cur+node.val)
            helper(node.right,cur+node.val)
            if cur + node.val == sum:
                self.total +=1
            

        def dfs(node):
            if not node:
                return
            helper(node,0)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        return self.total
    
    #Optimal Solution
    class Solution:
        def pathSum(self, root: TreeNode, sum: int) -> int:
            self.total = 0
            self.lookup = defaultdict(int)
            self.lookup[sum] = 1
            def dfs(node,root_sum):
                if not node:
                    return
                root_sum += node.val
                self.total += self.lookup[root_sum]
                self.lookup[root_sum+sum] += 1
                dfs(node.left,root_sum)
                dfs(node.right,root_sum)
                self.lookup[root_sum+sum] -= 1

            dfs(root,0)

            return self.total