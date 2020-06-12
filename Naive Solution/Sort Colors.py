'''
    Rumtime: 
        time: while loop takes O(n), n is the length of nums, the for loop inside while takes O(n). 
        so total takes O(n**2)
        space: O(1) since no extra space needed
    Analysis: 
        Given: a list of int
        Ask: sort the list so all 0 go before all 1 before all 2
        Input: [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]
        To accomplish this: set a counter to record what we are searching for in each loop. s keeps track of 
        the index until which the list is sorted. iterate the list, and inside the while loop, set another loop
        starting from the current index of s, and when value at j == counter, swap values at j and values at s,
        and increase s by 1 because s + 1 elements in the list are now sorted. each iteration in the while loop
        also needs to increase counter by 1 to update what value we are looking for in the next iteration.
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0; s = 0; length = len(nums)
        while s < length:
            for j in range(s, length):
                if nums[j] == counter:
                    nums[s], nums[j] = nums[j], nums[s]
                    s += 1
            counter += 1
                
