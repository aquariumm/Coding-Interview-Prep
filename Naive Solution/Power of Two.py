'''
    Runtime: 
        time: a reverse process of binary search, O(logn)
        space: O(1), no extra space needed
    Analysis:
        Given: an integer
        Ask: determine if this integer is a power of two
        Input: 1
        Output: true
        To accomplish this: first check any value <= 0 can't be a power of two. 
        have a while loop to multiple 2 until the resulting value great then the integer given. If in this 
        iteration, resulting value equals to the integer, which mean the integer can be written as 
        a power of two  then return True, else return False
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:   return False
        if n == 1:  return True
        result = 2
        while result <= n: 
            if result == n:
                return True
            result *= 2
        return False
