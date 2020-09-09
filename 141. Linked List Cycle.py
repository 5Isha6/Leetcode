#141. Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        node = head
        # print("original ",node)
        if node is None:
            return False
        elif node.next is None:
            return False
        while node:
            # print(node)
            if node.val == 10^6:
                return True
            node.val = 10^6
            node = node.next
            
        return False
        
        