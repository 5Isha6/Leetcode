# 110. Balanced Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def get_ht(root):
            if root is None:
                return -1
            else:
                return max(get_ht(root.left),get_ht(root.right))+1
            
        if not root:
            return True
        
        return abs(get_ht(root.left) - get_ht(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
