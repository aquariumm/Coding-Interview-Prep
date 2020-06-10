'''
    Rumtime: 
        time: to iterate s take O(n), n is the length of s, inside the loop, to find new_index take O(m), 
        m is the length of t. total takes O(mn)
        space: t_list is allocated and takes O(m). m is the length of t
    Analysis:
        Given: two strings s and t
        Ask: check if s is a subsequence of t
        Input: s = 'abc', t = 'aabbcc'
        Output: true
        To accomplish this: iterate string s from first to last char, if any char can't be found in t_list, 
        it means a char is not in string t so return False. else keep looping. One trick here is the check of
        char i should resume from the previous index where the previous char is found, instead of from index 0 
        again in t_list. 
'''
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:   return True 
        if not t and s:   return False
        t_list = list(t)
        prev_index = 0
        for i in s: 
            try:
                # here add prev_index to the index of sublist to make sure the value of new_index is in regard
                # to is the total length of t_list and not the sublist t_list[prev_index] 
                new_index = t_list[prev_index:].index(i) + prev_index
            except:
                return False
            else:
                # in case 
                if new_index >= len(t): return False
                prev_index = new_index + 1
                
        return True
