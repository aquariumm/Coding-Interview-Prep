class Solution:
    def numberOfMatches(self, n: int) -> int:
        match = 0
        while n > 1: 
            match += n // 2
            n = (n + 1) // 2
        
        return match
