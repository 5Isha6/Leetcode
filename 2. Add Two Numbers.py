# 2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # write your code here
        reversed_n1 = int(self.find_num(l1))
        reversed_n2 = int(self.find_num(l2))
       
        n = reversed_n1 + reversed_n2
        n = str((str(n)[::-1]))
        
        
        dummy = ListNode(0)
        curr = dummy
         
        if int(n) == 0:
            return dummy
        
        while len(n) != 0:
            num = n[0]
            curr.next = ListNode(int(num))
            n = n[1:]
            curr = curr.next
                               
        return dummy.next

    def find_num(self,l1):    
        
        n = ''
        
        while l1 != None:
            n += str(l1.val)
            l1 = l1.next
    
       
        return str(n)[::-1]
