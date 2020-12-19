'''
    Runtime: 
        time: the helper function traverses all nodes in the binary tree, potentially it takes O(2**n), n is the level 
        of the given tree, the sum and max used in the return statement takes less time than helper function, 
        so total is O(2**n)
        space: track takes O(n), n is the level of given tree. O(n)
    Analysis: 
        Given: a binary tree
        Ask: sum of values of its deepest leaves
        Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
        Output: 15
        To accomplish this: build a dict, key being the level number, and values being node value at that specific level. 
        with this, it is easy to find the answer by find the max key in the dict and sum all values at that key. 
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        track = defaultdict(list)
        
        def helper(node, level):
            if getattr(node, 'left', None):
                helper(node.left, level+1)
            if getattr(node, 'right', None):
                helper(node.right, level+1)
            if not getattr(node, 'left', None) and not getattr(node, 'right', None):
                track[level].append(node.val)
                
        helper(root, 0)
            
        return sum(track[max(track)])
