'''
    Runtime: 
        time: depends on values of each freq
        space: depends on values of freq
    Analysis:
        given: a list of integers, which can be divided into pairs. First value in each pair is 
        freq, and second value of each pair is val that needs to repeat freq times
        ask: return a list based on freq and value
        Input: nums = [1,1,2,3]
        Output: [1,3,3]
        To accomplish this: trick here is increment ind in range by 2 each time, and another trick is construct 
        a list that repeat nums[ind] time in each loop
'''
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:            
        return [val for ind in range(0,len(nums)-1,2) for val in [nums[ind+1]] * nums[ind] ]
        
