#919. Complete Binary Tree Inserter
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.deque  = deque()           
        self.q = deque([root])
        self.root = root
        
        while self.q:
            node = self.q.popleft()
            if not node.left or not node.right:
                self.deque.append(node)
            if node.left:
                self.q.append(node.left)
            if node.right:
                self.q.append(node.right)
                # self.deque.popleft()
        
        
        
    def insert(self, val: int) -> int:
        newNode = TreeNode(val)
        self.deque.append(newNode)
        curr = self.deque[0]
        
        if not curr.left:
            curr.left = self.deque[-1]
        else: #not curr.right:
            curr.right = self.deque[-1]
            self.deque.popleft()
        return curr.val
        
        
    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
