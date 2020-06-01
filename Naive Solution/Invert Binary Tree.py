'''
    Runtime:
        time: recursively calling from first node to the last takes O(n). n is the total number of nodes
        space: recursive stack takes O(n), n is the total number of nodes
    Analysis:
        Given: a binary tree
        Ask: invert it 
        Input: [1,2,3]
        Output: [1,3,2]
        To accomplish this: idea here is we want to swap positions of original left and original right. 
        recursion is usually easier to deal with tree structures and we can leverage recusions in this case.
        recusions will keep going until nodes that do not have left and right nodes. aka the leaf nodes. then
        it return back to its parent node but swap the position of it, i.e. if it was the left leaf node, now
        it becomes the right left node of its parent node. by doing so all subtrees will be inverted.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return 
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        
        return root
