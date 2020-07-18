'''
    Rumtime: 
        time: O(nlogn). consturct d requires looping nums, which takes O(n). the sorted function takes O(nlogn), 
        so the determinant is O(nlogn)
        space: O(n), O(n) to construct a dict and O(k) to store sorted return values
    Analysis: 
        Given: a list of int, and k is number of most common int from the given list
        Ask: return first to kth most common int from the given list
        Input: nums = [1,1,1,2,2,3], k = 2
        Output: [1,2]
        To accomplish this: first build a dict, key being unique int in the given list, and values being respective 
        occurrence in the list. Then sort the dict by values and add keys to another list in the order of most common
        to least common until the number of int in this list equals to the given k. then return the list
'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if set(nums) == k:
            return list(set(nums))
        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1
        l = []
        for i in sorted([i for i in d.items()], key=lambda x: x[1], reverse=True):
            print(i)
            if len(l) < k:
                l.append(i[0])
            
        return l
        
