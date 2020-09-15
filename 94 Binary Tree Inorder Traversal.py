# 94 Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
	
	  result = []
        stack = []
        while root != None:
            while root != None or stack != []:
                while root != None:
                    stack.append(root)
                    root = root.left
                root = stack.pop()
                result.append(root.val)
                root = root.right
        
        return result
        
		
        # result = []
        # # curr = root
        # def traverse(curr):
            # if curr == None:
                # return
            # else:
                # traverse(curr.left)
                
                # result.append(curr.val)
                # traverse(curr.right)
        # traverse(root)
        # return result
        
        
   
        
            