'''
    Runtime: 
        time: traversing all nodes takes O(n)
        space: q stores all nodes, takes O(n)
    Analysis:
        given: root of a n-ary tree
        ask: maximun depth
        Input: root = [1,null,3,2,4,null,5,6]
        Output: 3
        To accomplish this: bfs is one way of solving it, so a queue is needed. 
        store all nodes from the same depth to a list, and then add this list to the queue. while q exists, 
        we need to continue iterations, and each time we pop the queue, we will get a list of previous nodes. 
        and each iteration means a level increase. One thing to note is when len(temp) becomes 0, it means no more 
        nodes, since temp is a list, in order to make the while loop work all the time, we have a special case there
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        res = 0
        q = collections.deque()
        q.append([root])

        count = 0
        while q: 
            res += 1
            node = q.popleft()
            temp = []
            for i in node:
                temp.extend(i.children)
            q.append(temp) if len(temp) > 0 else None            

        return res
