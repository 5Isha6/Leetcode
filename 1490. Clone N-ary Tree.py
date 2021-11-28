#1490. Clone N-ary Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        self.visit = {}
        
        def dfs(node):
            if node in self.visit:
                return self.visit[node]
            
            cl_node = Node(node.val,[])
            self.visit[node] = cl_node
            cl_node.children =  [dfs(n) for n in node.children]
            return self.visit[node]
        return dfs(root)
