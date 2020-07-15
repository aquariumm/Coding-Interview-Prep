'''
    Rumtime:
        time: O(n), n is the total nodes, because all nodes need to be traversed to decide if two trees are same
        space: O(n) since recursion stacks take spaces
    Analysis:
        Given: two trees
        Ask: return True if they are same False if not
        To accomplish this: start from both node, check if they are same, if not return False, if yes, traverse
        left node of the current node of both trees and same checks on right nodes. 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        if any([p, q]) is True and all([p, q]) is False:
            return False
        if p.val != q.val:
            return False
        else:
            if p is None:
                return True
            else:
                return all([self.isSameTree(p.left, q.left), self.isSameTree(p.right, q.right)])
