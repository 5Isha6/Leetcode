# 1485. Clone Binary Tree With Random Pointer
# Definition for Node.
# class Node:
#     def __init__(self, val=0, left=None, right=None, random=None):
#         self.val = val
#         self.left = left
#         self.right = right
#         self.random = random

class Solution:
    def copyRandomBinaryTree(self, root: 'Node') -> 'NodeCopy':
        
        
        self.visit = {}
        
        def dfs(node):
            
            if not node:
                return node
            
            if node in self.visit:
                return self.visit[node]
            
            cl_node = NodeCopy(node.val)
            self.visit[node] = cl_node
            
            cl_node.left = dfs(node.left)
            cl_node.right = dfs(node.right)
            cl_node.random = dfs(node.random)
            
            return self.visit[node]
        return dfs(root)
