'''
    Runtime:
        time: loop from the first node in the linked list to the last one, O(n)
        space: counter is used and no other space allocated, so O(1)
    Analysis:
        Given: a singly-linked list
        Ask: the problem asks to arrange a given singly-linked list such that node in odds number 
        position are put together and even numbered nodes are put together, and all even nodes 
        need to be placed after odd nodes. e.g. 
        Input: 1->2->3->4->5->NULL
        Output: 1->3->5->2->4->NULL
        To accomplish this: it can be observed that the original order of the given linked list is: 
        odd1->even2->odd3->even4->... the number following each node indicates if it is 
        in an even or odd position. From there we need to rearrange them so odd1.next = odd3, 
        and even2.next = even4 and so on 
        For any node, if we have the current node (head) and its next node (head.next), we then know 
        in the new arrangement the next node of head.next (node.next.next) should be appended to 
        current node
        we assign node.next = node.next.next, this assignment holds true for every node in the list, 
        and by looping through the list, we will have odd1->odd3->odd5... and even2->even4->even6...
        then append even to odd will be the answer
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        '''
            group nodes by even and odd their positions, then odd number followed by even number
        '''
        # if list is empty: return False
        if not head:    return 
        # if there is only one node: return itself
        if not head.next:   return head
        # save the the first node and second node, first is the beginning of the entire list, 
        # and second is the beginning of the even number group, after iteration, 
        # second needs to be appended to the last node in odd numbered group
        # and first will be returned.
        # counter is needed to distinguish the total number of nodes in the list, 
        # e.g. if there are 3 nodes in the list, by the end of the loop, the node is the last odd node, 
        # so head.next = sec will give what is needed, but when the total number is even, after iteration, 
        # the last node is at even node, so if node.next = sec, we get a circle that the first node in 
        # the even number group is appended to the last node in the even number group, to avoid this, 
        # the counter is used
        fir, sec, counter = head, head.next, 1 
       
        while head and head.next:
            nex, head.next, prev = head.next, head.next.next, head
            
            head = nex
            counter += 1
        if counter % 2 == 0: 
            prev.next = sec
        else:
            head.next = sec
        return fir
