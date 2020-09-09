#19. Remove Nth Node From End of List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        dummy_node = ListNode()
        dummy_node.next = head
        p,f = dummy_node, dummy_node
        for i in range(n+1):
            f = f.next
        while(f != None):
            p = p.next
            f = f.next
            
        p.next = p.next.next
        
        return dummy_node.next              
    
       
        
        
        
        
        
 