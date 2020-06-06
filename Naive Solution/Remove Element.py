'''
    Runtime: 
        time: the loop takes O(n), n is the length of the nums list
        space: nums[i:] = nums[i+1:] takes O(m), m is the slicing length. and it can be up to O(n)
    Analysis:
        Given: a list of int, val that needs to be removed from the int list
        Ask: remove val from the nums list
        To accomplish this: we loop thru the nums list, when see val we shift everything to the right 
        of it one position to the left, so val gets replaced, and when we do such an operation, make sure
        to reduce the length by 1
'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        le = len(nums)
        while i < le:
            if nums[i] == val:
                nums[i:] = nums[i+1:]
                le -= 1
            else:
                i += 1
        
