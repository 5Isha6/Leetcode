# 138. Copy List with Random Pointer
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def __init__(self):
        self.visit = {}
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        if head in self.visit:
            return self.visit[head]
        
        node = Node(head.val,None,None)
        self.visit[head] = node
        node.random = self.copyRandomList(head.random)
        node.next = self.copyRandomList(head.next)
        
        return node
