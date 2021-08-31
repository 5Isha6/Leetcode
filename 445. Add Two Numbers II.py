# 445. Add Two Numbers II
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # write your code here
        n1 = self.find_num(l1)
        n2 = self.find_num(l2)
       
        n = n1 + n2
        
        n = str(n)
        
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
        n1, n2 = 0, 0
        j = 0
        while l1 != None:
            n1 *= pow(10,j) 
            n1 += l1.val
            l1 = l1.next
            j = 1
        return n1
