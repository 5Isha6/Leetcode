# 1305 All Elements in Two Binary Search Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # print(root1, root2)
        def traverse(root):
            if root == None:
                return []
            else:
                return traverse(root.left) + [root.val] + traverse(root.right)
        
        return sorted(traverse(root1) + traverse(root2))