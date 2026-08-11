# Definition for a binary tree node.
 

class Solution:

    def check(self,root,mn,max):
        if root is None:
           return True
        if root.val > max or root.val < mn:
            return False
        left = self.check(root.left,mn,root.val - 1)       
        right = self.check(root.right,root.val + 1, max) 

        return left and right 

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.check(root,float("-inf"),float("inf"))