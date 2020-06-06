'''
    Runtime: 
        time: the loop takes O(n), n is the length of the nums list. slice of nums takes O(n - j),
        j is the index at which the slice starts
        space: nums[j:] takes O(n-j) space
    Analysis: 
        Given: a list of int
        Ask: remove duplicates and return the new length of the list
        Input: [1,1,2]
        Output: 2
        To accomplish this: use two pointers, j keeps track of unique values and i for looping the list.
        also set a prev to track what value is right before the current value so as to indentify if duplicates.
        if prev is not current, continue without doing anything, else, we know a new value shows up at the 
        current position i, so we can first assign prev to get this value, and then move j one position to 
        its right, this move is needed becuase j keeps track of unique values, and if we don't move, we 
        would replace a unique value, so we move j to its right and assign the value at position i, then 
        move i to its right by one position as well so to continue looping. After looping, we know in list nums, 
        up until j is all unique values, and everything after j is captured in nums[:j], so we remove everything
        after position j.
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 
        j = 0
        i = 0
        prev = nums[0]
        
        for i in range(len(nums)):
            if nums[i] == prev:
                
                continue
            else:
                prev = nums[i]
                j += 1
                nums[j] = prev
                i += 1
        nums[j:] = [nums[j]]
        
            
        
