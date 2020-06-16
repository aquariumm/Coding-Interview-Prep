'''
    Runtime: 
        time: binary search recursion takes O(logn), n is total number of nodes
        space: recursion stack takes O(n)
    Analysis: 
        Given: a binary tree, and a val
        Ask: return the node that has val == the given val, if not exists, return []
        To accomplish this: since binary tree is given, we can compare the current node val with the given 
        val, if the given val is larger, then we need to search in the right side of the current node. if 
        the given val is small, we need to search in the left side of the current node. This is due to the 
        binary tree attributes. If the current node val == given val, we can return this node, if there is 
        no more node since we have reached the leaf of this tree, we return []
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root: return 
        elif root.val == val: return root
        elif root.val < val: return self.searchBST(root.right, val)
        else: return self.searchBST(root.left, val)
        
