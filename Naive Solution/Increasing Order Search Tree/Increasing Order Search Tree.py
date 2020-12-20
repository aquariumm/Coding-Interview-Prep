'''
    Rumtime: 
        time: helper function takes O(n) to iterate all nodes, when constructing ans, it takes another O(n) to iterate
        res. so total O(n)
        space: res takes O(n), ans takes O(n)
    Analysis: 
        Given: root of a binary search tree
        Ask: return an in order travseral of the given tree
        Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
        Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
        To accomplish this: helper function will stores nodes in res by in order traversal. iterating res to contruct 
        needed new tree. 
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        
        def helper(node, res):
            if not node:
                return
            helper(node.left, res)
            res.append(node)
            helper(node.right, res)
        helper(root,res)
        
        ans = head = res[0]
        head.left = None
        for node in res[1:]:
            head.right = node
            node.left = None
            head = node
        
        return ans
