class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        if(root == None): return len(arr) == 0;
        return self.isValid(root, arr, 0);

    def isValid(self, root: TreeNode, arr: List[int], idx: int) -> bool:
        if(root.val != arr[idx]): return False;
        if(idx == len(arr)-1):
            return root.left == None and root.right == None;
        return ((root.left != None and self.isValid(root.left, arr, idx+1)) or (root.right != None and self.isValid(root.right, arr, idx+1)));
    