'''
    Runtime:
        time: the possibility of traversing all nodes in original tree takes O(n), so total O(n)
        space: orgStack and clnStack take extra space, depends on the depth of trees
    Analysis:
        given: two binary trees, original and cloned, and a target that is from original tree
        ask: return the node from cloned tree that is in the same position as in the original tree
        Input: tree = [7,4,3,null,null,6,19], target = 3
        Output: 3
        to accomplish this: DFS is useful here, while traversing nodes in the original, traverse cloned tree 
        with same pace and return node in the cloned tree when target node is found in the original tree.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        orgStack = [original]
        clnStack = [cloned]
        
        while orgStack:
            node = orgStack.pop()
            res = clnStack.pop()
            
            if node == target:
                return res
            if node.left:
                orgStack.append(node.left)
                clnStack.append(res.left)
            if node.right:
                orgStack.append(node.right)
                clnStack.append(res.right)
        
        return None
