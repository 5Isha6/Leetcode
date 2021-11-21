#426. Convert Binary Search Tree to Sorted Doubly Linked List
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        
        
        def helper(curr):
            nonlocal first, last
            if curr:
                helper(curr.left)

                if last:
                    last.right = curr
                    curr.left = last
                else:
                    first = curr
                last = curr
                
                helper(curr.right)
        
        if not root:
            return None
        first, last = None, None
        helper(root)
        
        last.right = first
        first.left = last
        return first
        
