# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newList = []
        node = head
        while node:
            newList += [node.val]
            node = node.next
        newList = newList[::-1]
         
        dummy = ListNode(0)
        node = dummy
    
        for num in newList:
            node.next = ListNode(num)
            node = node.next
        return dummy.next




        