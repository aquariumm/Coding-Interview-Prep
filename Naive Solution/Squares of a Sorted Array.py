'''
    Rumtime: 
        time: sorted() takes O(nlogn), n is the length of list A. looping through list A to 
        get the squares of each number takes O(n)
        space: sorted() takes O(n) space to operate
    Analysis: 
        Given: a sorted list of integers in ascending order
        Ask: return a list of squares of each number in ascending order 
        Input: [-4,-1,0,3,10]
        Output: [0,1,9,16,100]
        To accomplish this: we can loop through to calcuate squares of each number and assign values,
        then use sorted() on the list to return 
'''
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        for i in range(len(A)):
            A[i] = A[i]**2
        return sorted(A)
        
