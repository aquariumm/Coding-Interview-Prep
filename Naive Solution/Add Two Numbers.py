'''
    Rumtime: 
        time: O(max(l1, l2)). Iterating l1 and l2 is needed for this calculation. Since each node is needed
        to be visited, O(l1) and O(l2) time is needed to traverse l1 and l2, the two traversals are parallel 
        to each other, thus the max of the two will be dominant in determining the time complexity
        space: a seperate linklist is maintained so O(max(l1,l2)+1), l1 and l2 is the total number of nodes 
        in l1 and l2. An analogy is imagine adding two ints, the max result length will be the max of the 
        two operands + 1
    Analysis:
        Given: two linkted lists representing two integers
        Ask: return the sume of the two given integers
        Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
        Output: 7 -> 0 -> 8
        To accomplish this: iterating two linked lists and sum each node from the two lists. Key here is to 
        consider all cases
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(a, b, rem):
            if not (a or b or rem): return
            if a: # a exist
                if b: # b exist
                    tem = a.val + b.val + rem
                    if tem < 10:
                        val = ListNode(tem)
                        val.next = helper(a.next, b.next, 0)
                        
                    else: # tem >= 10
                        val = ListNode(tem % 10)
                        val.next = helper(a.next, b.next, 1)
                    return val
                else: # a exist, b not
                    tem = a.val + rem
                    if tem < 10:
                        val = ListNode(tem)
                        val.next = a.next
                    else: # tem >= 10
                        val = ListNode(tem % 10)
                        val.next = helper(a.next, b, 1)
                    return val
            else: # a not exist
                if b: # a not, b exist
                    tem = b.val + rem
                    if tem < 10:
                        val = ListNode(tem)
                        val.next = b.next
                    else: 
                        val = ListNode(tem % 10)
                        val.next = helper(a, b.next, 1)
                    return val
                else: # a not, b not
                    if rem:
                        val = ListNode(rem)
                        return val
                    else:
                        return 
        return helper(l1, l2, 0)
