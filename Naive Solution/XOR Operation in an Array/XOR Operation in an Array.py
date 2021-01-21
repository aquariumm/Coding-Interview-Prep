class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        res = [start+2*i for i in range(n)]
        r = res[0]
        for i in res[1:]:
            r ^= i
        return r
