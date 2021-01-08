'''
    Runtime: 
        time: iterating both trees takes O(max(n, m)), n and m are number of nodes in two trees
        space: O(1) since no extra space needed
    Analysis:
        given: two binary tree
        ask: return a tree, of which nodes are sum of the given two trees in same positions
        input: [1,3,2,5]
        [2,1,3,null,4,null,7]
        output: [3,4,5,5,4,null,7]
        to accomplish this: recursively traversing all nodes and sum two nodes in same postions in each recursion call
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, l1: TreeNode, l2: TreeNode) -> TreeNode:
        if not l1 and not l2:
            return 
        if l1 and not l2:
            return l1
        if l2 and not l1:
            return l2

        l1.val = l1.val + l2.val
        l1.left = self.mergeTrees(l1.left, l2.left)
        l1.right = self.mergeTrees(l1.right, l2.right)

        return l1
        
        
