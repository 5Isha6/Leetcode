#234. Palindrome Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node = head
        slow = head
        fast = head
                
        while fast != None and fast.next != None:
            # second = node.next
            slow = slow.next
            fast = fast.next.next
        # print('print(slow,fast)   ',slow,fast)   
        if fast != None:
            mid = slow.next
        else:
            mid = slow
        # print('mid ', mid)   
        prev,next_ = None, None
        while mid != None:
            next_ = mid.next
            mid.next = prev
            prev = mid
            mid = next_
        # print('prev ',prev)
        
        while prev != None:
            if prev.val != head.val:
                return False
            prev= prev.next
            head = head.next
        
        return True
        