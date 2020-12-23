'''
    Runtime:
        time: traversing each node takes O(n)
        space: storing all nodes takes O(n)
    Analysis:
        given: a perfect binary tree
        ask: populate each node next pointer to its right node. If not right node, use None
        Input: root = [1,2,3,4,5,6,7]
        Output: [1,#,2,3,#,4,5,6,7,#]
        To accomplish this: bfs can be used for this. group all nodes from the same level to a list, and append this 
        list to queue. while queue exists, iterating all nodes from same level and special case is when last node, its
        next is None, another special case is when temp is empty which means no more nodes to add, in which case 
        we do not add empty list in order for the while loop to work.
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        q = collections.deque()
        q.append([root])
        
        while q:
            node = q.popleft()
            temp = []

            for i, n in enumerate(node):
                if i == len(node) - 1:
                    n.next = None
                else:
                    n.next = node[i+1]
                if n.left:
                    temp.append(n.left)
                if n.right:
                    temp.append(n.right)
                
            q.append(temp) if len(temp) > 0 else None

        return root
        
