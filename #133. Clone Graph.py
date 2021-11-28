#133. Clone Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        self.q  = [node]
        self.visit = {}
        
        self.visit[node] = Node(node.val,[])
        while self.q:
            curr = self.q.pop()
            
            for n in curr.neighbors:
                if n not in self.visit:
                    
                    cl_node  = Node(n.val,[])
                    self.visit[n] = cl_node
                    self.q.append(n)
                    
                self.visit[curr].neighbors.append(self.visit[n])
        
        return self.visit[node]
        
        
        
        
        
        #M2 dfs
#         self.visit = {}
#         def dfs(node):
        
#             if not node:
#                 return node
        
#             if node in self.visit:
#                 return self.visit[node]

#             else:
#                 cl_node = Node(node.val,[])    
#                 self.visit[node] = cl_node
#                 if node.neighbors:
#                     cl_node.neighbors = [ dfs(n) for n in node.neighbors]
#                 return cl_node
#         return dfs(node)
