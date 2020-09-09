#1022 Sum of Root To Leaf Binary Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        total = 0
        def dfs(node, current):
            if node is None:
                return 0
            
            current = current * 2 + node.val
            # print(current)
            if node.left is None and node.right is None:
                nonlocal total 
                total += current
                return
            
            dfs(node.left,current)
            dfs(node.right,current)
            
        dfs(root,0)
        return total
        
                
        