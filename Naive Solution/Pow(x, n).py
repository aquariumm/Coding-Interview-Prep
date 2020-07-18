'''
    Runtime: 
        time: O(logn), n is the n given in the function. Each time recursion happens, only half of n is calculated. 
        so until n becomes 0, logn recursion calls are made
        space: O(logn), recursion stack takes O(logn) space because of the depth it needs. to reach n == 0, a 
        binary tree needs to be stored, and thus O(logn)
    Analysis:
        Given: x and n, x is the base and n is the power
        Ask: calculate the value of x**n
        Input: 2.10000, 3
        Output: 9.26100
        To accomplish this: straight forward thinking might be recursively call the function and in each time call, 
        keep x the same, and n - 1, the return value being x multiples the recursion function. and recursion exit
        condition is when n == 0, and return 1. Or maybe loop from 0 to n, and each iteration will make x multiples 
        itself one more time. Both will exceed time limit, another approach is through the fact x**n = (x**n/2) ** 2.
        depending on n is even or odd, an extra x might need to be multiplied. 
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n > 0:
            if n % 2 == 0:
                return self.myPow(x, n//2)**2
            else:
                return self.myPow(x, n//2) ** 2 * x
        else:
            if n % 2 == 0:
                return self.myPow(x, -(-n//2))** 2
            else:
                return self.myPow(x , -(-n//2))**2 * 1/ x
        
