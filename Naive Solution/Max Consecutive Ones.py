'''
    Rumtime: 
        time: iterate over the nums list. O(n), n is the length of nums list
        space: O(1) since no extra space allocated
    Analysis: 
        Given: a list of number. 0 and 1 only
        Ask: find the longest subset of consecutive 1s
        To accomplish this: we can have two variables, one keep track of the local subset, one tracks the global 
        max subset. local subset starts from when we see the first 1 to when we see the last 1 in nums, 
        and global max is the longest subset we have seen so far until the current position. 
        i.e. we loop through the nums list, if we see 1, we add 1 to the local max subset 
        variable, if we see 0, we assign the global max = max(global max, local max) and set local max = 0
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m = 0; loc_m = 0
        for i in nums:
            if i == 0:
                m = max(m, loc_m)
                loc_m = 0
            else:
                loc_m +=1
        # in case nums contains [1], max(m, loc_m) will return correct answer
        return max(m, loc_m)
        
