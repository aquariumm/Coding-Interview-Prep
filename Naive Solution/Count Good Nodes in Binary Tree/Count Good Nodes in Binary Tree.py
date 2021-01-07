'''
    Runtime: 
        time: traversing all nodes takes O(n+v), n is total number of nodes, v is all edges
        space: O(1) since no extra space allocated
    Analysis:
        given: a binary tree
        ask: find total number of nodes, which have val no less than than all their previous nodes 
        Input: root = [3,1,4,3,null,1,5]
        Output: 4
        to accomplish this: DFS is useful in this case, values saved in left and right represent the number of 
        qualified nodes to the left and to the right of the current node that we are at.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, curMax):
            locMax = max(curMax, node.val)
            left = dfs(node.left, locMax) if node.left else 0
            right = dfs(node.right, locMax) if node.right else 0
            
            return left + right + (node.val >= curMax)
        
        return dfs(root, root.val)
        
