'''
    Runtime:
        time: O(1) since replacing current node with its next node is the only operations
        space: O(1) no extra space is used
    Analysis: 
        Given: a node that needs to be deleted from a linked list
        Ask: remove the given node
        To accomplish this: we are only given the node that needs to be deleted, we know this node 
        is somewhere in a linked list. we know nothing about what's before this node, but we have info
        about what's after this node. we can replace the current node value with the value of its next 
        node, aka node.next.val, by doing so we have current node and its next node both have same value, 
        so we can consider this linked list have two identical nodes, and the current node is gone since its
        value has been replaced. we then let node.next to be node.next.next, this produce one less node than 
        the original linked list and the removed node is the second node from the two identical nodes we 
        made. This process is equvalent to deleting the given node
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:    return 
        node.val = node.next.val
        node.next = node.next.next
        
