class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        res, l = [], list(range(1, m+1))
        for i in queries:
            ind = l.index(i)
            res.append(ind)
            l = [i] + l[:ind] + l[ind+1:]
        return res
