class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        for i in range(len(candies)):
            local = candies[i] + extraCandies
            res.append(local >= max(candies))
        
        return res
        
