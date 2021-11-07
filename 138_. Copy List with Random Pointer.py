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
    def copyRandomList(self, head: 'Node') -> 'Node':
        
        cur = head
        mapping = {None:None}
        
        while cur:
            
            new_node = Node(cur.val)
            mapping[cur] = new_node
            cur = cur.next
        
        cur = head
        while cur:
            new = mapping[cur]
            new.next = mapping[cur.next]
            new.random = mapping[cur.random]
            cur = cur.next
        
        return mapping[head]
            
            

            
            
        
