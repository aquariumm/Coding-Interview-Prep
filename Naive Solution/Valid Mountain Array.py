'''
    Runtime: 
        time: for loop takes O(n), n is the length of A
        space: no extra space, so O(1)
    Analysis: 
        Given: a list of int
        Ask: if this list is a mountain shape. e.g.
        Input: [0,3,2,1]
        Output: true
        To accomplish this: first find the pivot where the mountain peak is. If the peak is i then i-1 < i 
        and i > i + 1. if this list is a true mountain shape, all points before the peak should be strictly 
        increasing and all point after the peak should be strictly decreasing. To find the peak, we can 
        iterate the list until the index where value at index + 1 < value at index. Then we need to verify that 
        all points after the peak strictly decrease. so start from index i all the way to len(n) - 1, if there
        exists value at index + 1 >= value at index then return False, else return True
'''
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3: return False
        for i in range(len(A)-1):
            if A[i+1] <= A[i]:
                break
        if i == 0: return False
        for j in range(i, len(A)-1):
            if A[j+1] >= A[j]:
                return False
        return True
