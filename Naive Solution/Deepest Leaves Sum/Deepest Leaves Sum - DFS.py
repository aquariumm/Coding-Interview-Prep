'''
    Runtime: 
        time: the while loop iterates each node in the tree, and take O(n)
        space: stack takes O(n) to store all nodes
    Analysis: 
        Given: a binary tree
        Ask: sum of values of its deepest leaves
        Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
        Output: 15
        To accomplish this: use DFS, each time a node is added, it means the height of this subtree has increased by 1.
        if the height at this iteration is less than the maxLevel, we know we can ignore this value since it is not 
        the deepest node, if its height equals to maxLevel, it satisfies the condition and we can add it to res, and 
        if its height is greater than maxLevel, we reset maxLevel and res to use this node's.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        res = 0
        maxLevel = 0
        stack = [(root, 0)]
        
        while stack:
            node, level = stack.pop()
            
            if level > maxLevel:
                maxLevel = level
                res = node.val
            elif level == maxLevel:
                res += node.val
                
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        
        return res
