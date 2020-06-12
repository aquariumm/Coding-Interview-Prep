'''
    Runtime: 
        time: the for loop takes O(n), and the max function takes O(n-i), so total is O(n**2), n is the 
        length of arr
        space: O(1), no extra space
    Analysis:
        Given: a list of int
        Ask: replace value at each index with the max of value from the sub list starting from index + 1
        Input: arr = [17,18,5,4,6,1]
        Output: [18,6,6,6,1,-1]
        To accomplish this: loop through the arr and at each index, find the max of the sublist to its right
        and replace the current value with this max value from sublist
'''
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)-1):
            arr[i] = max(arr[i+1:])
        arr[-1] = -1
        return arr
        
