'''
    Runtime:
        time: Counter is a built-in function, it should be optimized, but worst case, it will take O(n)
        for its operations. the for loop iteration take O(n), inside the loop, s_par take O(n),
        the two all() operations take O(n) because of the iteration inside of it. In total, O(n**2)
        space: a res list is allocated which can take up to the length of s, so O(n)
    Analysis:
        Given: two parameters: a string s and a non-empty string p. both strings are guaranteed to be
        English letters
        Ask: find all start indices of p's anagrams in s and return a list containing them. e.g.
        Input: s: "cbaebabacd" p: "abc"
        Output: [0, 6]
        To accomplish this: we can divide s into multiple partitions, each of which is of len(p) -> s[i:i+len(p)]
        compare each partition with p to validate if this partition is an anagram of p. use Counter() here, e.g
        p_arrange will construct a dict with elements in p as keys and counts of each element as values, same for s_par
        two checks needed:
            first, validate keys in s_par are in p_arrange, and vice verse -> all(j in p_arrange for j in s_par), all(j in s_par for j in p_arrange)
            second, validate counts of each key in s_par match p_arrange -> all(s_par[j] == p_arrange[j] for j in s_par)
        if so, append to res
        return res after looping string s
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # validate s and p are valid inputs. if len(p) > len(s) also not valid since there is no way 
        # to find anagrams of a longer string from a shorter string.
        if not s or len(s)<len(p) or not p:   return 
        # construct p_len, p_arrange, res
        p_len = len(p); p_arrange = Counter(p); res=[]
        for i in range(0, 1+len(s)-p_len):
            s_par = Counter(s[i:i+p_len])
            # validate in s_par and in p_arrange have same keys, if not move on to next partition
            if not all(j in p_arrange for j in s_par) or not all(j in s_par for j in p_arrange):
                continue
            # if reach here, it means s_par and p_arrange have same keys, so if the values of each key in s_par is the 
            # same as in p_arrange, it indicates s_par is an anagram of p_arrange, and this index should be added to res
            if all(s_par[j] == p_arrange[j] for j in s_par):
                res.append(i)
        return res
            
