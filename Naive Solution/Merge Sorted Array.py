'''
    Rumtime: 
        time: while loop takes O(m). nums1[i:] = [nums2[j]]+nums1[i:-1] takes amortized O(m). So total O(m^2).
        space: nums1[i:] = [nums2[j]]+nums1[i:-1] takes O(m) space
    Analysis:
        Given: two sorted int lists and the length of each. nums1 is guranteed to be longer than nums2
        Ask: merge two list into one. do so in place
        Input:
        nums1 = [1,2,3,0,0,0], m = 3
        nums2 = [2,5,6],       n = 3
        Output: [1,2,2,3,5,6]
        To accomplish this: we can loop through two lists. both start at index 0. if nums1[i] < nums2[j]
        we do nothing and continue. if nums1[i] >= nums2[j], then we  do [nums2[j]]+nums1[i:-1], which puts
        the current nums2[j] to the front of remaining nums1[i], and reassign nums1[i:] = this list. 
        the nums1[i:] covers the index from i to the end of nums1 list, and whenever such operation happens, 
        we need to make sure we add 1 to m as well, because think of what m represents, m is the length of 
        nums1, we added a value from nums2 to nums1 list so we need to add 1 to m to reflect such a change.
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        j = 0
        i = 0
        while i < m:
            if j >= n:
                break
            if nums1[i] == 0 and i >= m:
                
                nums1[i:] = nums2[j:]
                break
            else:
                if nums1[i] < nums2[j]:
                    i+= 1
                else:

                    nums1[i:] = [nums2[j]]+nums1[i:-1]
                    j+=1
                    i+=1
                    m+=1
                   
