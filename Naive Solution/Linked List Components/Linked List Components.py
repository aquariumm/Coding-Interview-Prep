'''
    Runtime: 
        time: len(res) takes O(1) by design. the for loop that populate values for temp list takes O(n), 
        n is the size of G, the while loop that iterates the linked list takes O(m), m is the size of 
        the given linked list. Since G is a subset of linked list, n < m. so total O(m)
        space: temp takes a constanct space because it is always allocated by 10000. res takes O(n), n is the number of 
        sublists in res. 
    Analysis: 
        given: head of a linked list, which contains only unique interger values, and a list that contains some values 
        from this linked list
        ask: return the number of connected components
        Input: 
        head: 0->1->2->3
        G = [0, 1, 3]
        Output: 2
        To accomplish this: we can construct a temp list, of which index represents values that can show up in the linked   
        list, since it is given in the question that the value of each node in the linked list will be in [0, N - 1], 
        we can set a finite size for temp, i.e. * 10000. and each value of this temp represents if the current index is
        in G. The purpose of temp is for easy retrieval while loop the linked list. When iterating the linked list, 
        check if the current node.value is in temp, if it is, then check if prev node.value is also in temp, if so append
        current node.value to the last sublist in res, if not, add a new sublist starting with current node.value to res.
        calculate the length of res will return the answer.
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        res = []
        prev = 0
        temp = [0] * 10000
        
        for i in G:
            temp[i] = 1
        
        while head:
            if temp[head.val]:
                if prev:
                    res[-1].append(1)
                else:
                    res.append([1])
                prev = 1
                
            else:
                prev = 0
            
            head = head.next
        
        return len(res)
