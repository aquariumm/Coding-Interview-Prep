'''
    Runtime: 
        time: outer loop takes O(n), inner loop takes O(n-i), total is O(n**2)
        space: no extra space needed, O(1)
    Analysis: 
        Given: a list of int
        Ask: return true if there exists an int in the list that is half of another int in the list
        Input: [2, 1, 3, 7]
        Output: true
        To accomplish this: outer loop iterates from index 0, and inner loop iterate from where outer loop 
        index is. At index i, outer loop get a value and assign it to cur, now check all int to the right of
        this index and see if there is a value that is either half of cur or double or cur.
'''
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        # special case for multiple 0
        if arr.count(0) > 1:
            return True
        for i in range(len(arr)):
            cur = arr[i]
            if cur == 0:
                continue
            for j in range(i, len(arr)):
                # since spacial case of 0 is validated before, here make sure no 0 is involved
                if arr[j] != 0 and (arr[j] == 2 * cur or arr[j] * 2 == cur):
                    return True
        return False
        
