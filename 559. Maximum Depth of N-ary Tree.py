# 559. Maximum Depth of N-ary Tree
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if not root:
            return 0
        elif not root.children:
            return 1
        ht = []
        for c in root.children:
            ht.append(self.maxDepth(c))
        return max(ht) + 1
        
