# 314. Binary Tree Vertical Order Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dic = collections.defaultdict(list)
        q = deque([(root,0)])
        
        while q:
            n, c = q.popleft()
            if n is not None:
                dic[c].append(n.val)
                q.append([n.left, c - 1])
                q.append([n.right, c + 1])
        
        return [dic[c] for c in sorted(dic.keys())]
        
