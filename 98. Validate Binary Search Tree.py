# 98. Validate Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # print(root, root.left,root.right)
        def isValid(root, left = float(-inf), right = float(inf)):
            if root is None:
                return True
            
            if not (lower < root.val < right):
                return False
            
            return isValid(root.left, min(left,root.val), right) and isValid(root.right, left, min(root.val, right))
            
        
