# 23. Merge k Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k = len(lists)
        q = PriorityQueue(maxsize = k)
        dummy = ListNode(0)
        curr = dummy
        for i,node in enumerate(lists):
            if node:
                q.put((node.val,i,node))
        while q.qsize() > 0:
            
            temp = q.get()
            curr.next,i  = temp[2], temp[1]
            curr = curr.next
            if curr.next:
                q.put((curr.next.val,i,curr.next))
        return dummy.next
