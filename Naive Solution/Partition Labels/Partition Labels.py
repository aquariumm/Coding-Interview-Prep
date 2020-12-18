'''
    Runtime: 
        time: allUnique function untilizes set() which takes max(O(scanned), O(remain)), the for loop in allUnique
            takes another O(scanned), the while loop in partitionLabels takes O(n). If the while loop iterates 
            each value in the given list, the amortized total time is O(n**2)
        space: res takes O(n), allUnique function take max(O(scanned), O(remain)). Total is O(n)
    Analysis: 
        Given: a string of all lowercase letters
        Ask: partition the given string into as many parts as possible but each letter in the string 
            appears at most once in a part
        Input: S = "ababcbacadefegdehijhklij"
        Output: [9,7,8]
        To accomplish this: the idea is a partition is valid if letters in the partition does not 
            appear in the remaining part of the given string, so allUnique is used. Then iterate values
            in partitionLabels, and take care of the case when j exceeds the bountry, in which case append
            the length of scanned, because None does not contain all letter
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        length = len(S)
        i = 0
        res = []
        
        while i < length:
            for j in range(i+1, length+1):
                scanned = S[i:j]
                remain = S[j:]
                
                if not remain:
                    res.append(len(scanned))
                    return res
                
                if self.allUnique(scanned, remain):
                    res.append(len(scanned))
                    i = j
                    break
        return res
    
    def allUnique(self, scanned, remain):
        scanned = set(scanned)
        remain = set(remain)
        
        for i in scanned:
            if i in remain:
                return False
        return True
