'''
    Runtime: 
        time: helper function iterates the given tree, takes O(n), n is the number of nodes. 
        iterating temp takes O(h), h is the height of the tree. So total is O(n)
        space: temp takes O(n)
    Analysis:
        given: root of a binary tree
        ask: return the level at which maximize the sum of nodes
        Input: root = [1,7,0,7,-8,null,null]
        Output: 2
        to accomplish this: use a dict to keep track of relations between level and nodes, key for level, 
        value for node.val. the find the level that has the max sum of node.vals
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        temp = defaultdict(list)
        res = 1
        currentSum = root.val
        
        def helper(node, level):
            temp[level].append(node.val)
            if node.left:
                helper(node.left, level+1)
            if node.right: 
                helper(node.right, level+1)
        helper(root, 1)
        
        for level, total in temp.items():
            if sum(total) > currentSum:
                res = level
                currentSum = sum(total)
        
        return res
