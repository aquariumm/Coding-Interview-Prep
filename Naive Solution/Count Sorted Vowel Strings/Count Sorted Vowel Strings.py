'''
    Runtime: 
        time: recursive calls determine the complexity here, and recusical calls are determined by i, since i decides  
        termination condition. by incrementing 1 at a time, time is O(n), n is the given integer.
        space: O(n) because there are total n level in the recrusion stack.
    Analysis:
        Given: an interger n
        Ask: return the possible ways to compose a string from vowels that is of length n and is in lexicographical order.
        Input: n = 1
        Output: 5
        To accomplish this: there's a math logic behind this question, as indicated in the helper function. There will 
        be iterations until i == n, and in this process, new a is the sum of previous a, b, c, d, e, and b is the sum of
        previous b, c, d, e, and so on. With this logic, we can solve the issue with recursion, with the excepition of 
        n == 1, which returns 5
'''

class Solution:
    def countVowelStrings(self, n: int) -> int:
        if n == 1:
            return 5
        return self.accumulateNum(5, 4, 3, 2, 1, 2, n)
        
    def accumulateNum(self, a, b, c, d, e, i, n):
        if i == n:
            return a + b + c + d + e
        return self.accumulateNum(a+b+c+d+e, b+c+d+e, c+d+e, d+e, e, i+ 1, n)
