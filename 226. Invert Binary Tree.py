# 226. Invert Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
    
        
        
#         if not root :
#             return None
        
#         def helper(root):
            
            
#             if not root or (not root.left and not root.right):
#                 return
#             temp = root.left 
#             root.left = root.right
#             root.right = temp
#             helper(root.left)
#             helper(root.right)
            
#         helper(root)
        return root
        
