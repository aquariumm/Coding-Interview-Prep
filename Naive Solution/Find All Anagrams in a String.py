'''
    Runtime:
        time: Counter is a built-in function, it should be optimized, but worst case, it will take O(n)
        for its operations. the for loop iteration take O(n), inside the loop, s_par take O(n),
        the two all() operations take O(n) because of the iteration inside of it. In total, O(n**2)
        space: a res list is allocated which can take up to the length of s, so O(n)
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or len(s)<len(p) or not p:   return 
        p_len = len(p); p_arrange = Counter(p); res=[]
        for i in range(0, 1+len(s)-p_len):
            s_par = Counter(s[i:i+p_len])
            if not all(j in p_arrange for j in s_par):
                continue
            if all(s_par[j] == p_arrange[j] for j in s_par):
                res.append(i)
        return res
            
