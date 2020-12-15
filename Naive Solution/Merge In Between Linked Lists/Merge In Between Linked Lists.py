# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        i = 0
        
        while list1:
            if i + 1 == a:
                start = list1
            if i - 1 == b:
                stop = list1
            i += 1
            list1 = list1.next
        
        start.next = list2
        while list2.next:
            list2 = list2.next
            
        list2.next = stop
        
        return head
