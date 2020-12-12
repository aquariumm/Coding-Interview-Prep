'''
    Runtime:
        time: O(n) since three loops are used
        space: res takes O(n), count takes O(1) since it's a finite length of 101
    Analysis:
        Given: an array
        Ask: return an array within which each number at a given index represents number of records in the 
        given array that are smaller than the value at same index in the given array
        Input: nums = [8,1,2,2,3]
        Output: [4,0,1,1,3]
        To accomplish this: structure a count list of length 101 and initialize with 0. In this list, an index 
        represents a value in the given list, and the value at that index in count list is the occurrence of that
        value. If a value is not in the given list, its default value is set to 0 in the count list. 
        the second loop does the trick to calculate number of records that are less than current index, aka. value in the 
        given list. the third loop add previous calculations into another list. Special case is considered when 
        nums[i] == 0, in which case its value is set to 0

'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        count = [0 for i in range(101)]
        
        for i in nums:
            count[i] += 1
        
        tem = 0
        for i in range(1, len(count)):
            count[i], tem = count[i-1] + tem, count[i]
        
        for i in range(len(nums)):
            if nums[i] == 0 :
                res.append(0)
            else:
                res.append(count[nums[i]])
            
                    
        return res
