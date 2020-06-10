'''
    Rumtime: 
        time: loop takes O(n), n is the length of nums
        space: O(1) since no extra space needed
    Analysis: 
        Given: a sorted list of int
        Ask: return the index of the list, at this index is either a value equal to target or the first 
        element that is greater than the target
        Input: [1, 3, 5], 2
        Output: 1
        To accomplish this: loop from the beginning of the list, if find the value == target, return the index
        if find the value > target: return the index
'''
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # in case the first elment in the list is greater than the target
        if nums[0] > target:    return 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i] > target:
                return i
        # in case all elements in the list is smaller than the target
        return len(nums) 
            
