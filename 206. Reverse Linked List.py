# 206. Reverse Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        node = head
        # ptr = ListNode(None)
        ptr = None
         
        while(node):
            
            t = node.next
            node.next = ptr
            ptr = node
            node = t
            
        return ptr
        
