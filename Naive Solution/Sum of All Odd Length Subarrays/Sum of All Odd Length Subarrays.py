class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        res = 0
        
        for i in range(len(arr)):
            sub = [arr[i]]
            res += sum(sub)
            for j in range(i+1, len(arr)):
                sub.append(arr[j])
                if len(sub) % 2 != 0:
                    res += sum(sub)
                    
        return res
