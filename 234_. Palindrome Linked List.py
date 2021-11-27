# 234. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        s, f = head, head
        while f and f.next:
            
            s = s.next
            f = f.next.next
            
        node = None            
        
        while s:
            
            t = s.next 
            s.next = node
            node = s
            s = t
            
        while node:
            if node.val != head.val:
                return False
            head = head.next
            node = node.next
        
            
            
            
            
            
            
        return True
