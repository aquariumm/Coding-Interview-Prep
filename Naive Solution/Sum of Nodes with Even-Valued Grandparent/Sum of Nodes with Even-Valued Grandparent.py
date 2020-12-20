'''
    Runtime: 
        time: while loop takes O(n)
        space: stack takes O(n)
    Analysis:
        Given: a binary tree
        Ask: sum of values of nodes that have even-valued grandparent nodes
        Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
        Output: 18
        To accomplish this: use DFS method, store nodes in a stack while iterationg the tree. node value should be 
        added to the result when its grdNode exists and has even value.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        
        stack = [(root, 0, 0)]
        while stack:
            node, parNode, grdNode = stack.pop()
            res += node.val if grdNode and grdNode.val % 2 == 0 else 0
            
            if node.left:
                stack.append((node.left, node, parNode))
            if node.right:
                stack.append((node.right, node, parNode))
            
        return res
