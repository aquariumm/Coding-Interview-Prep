'''
    Runtime: 
        time: there is a loop when building s1_count -> O(len(s1)), 
        the nested loop when building s2_count -> O(len(s1)*len(s2)), so total O(len(s1)*len(s2))
        space: s2_count and s1_count both take constant spaces of size 26
    Analysis:
        Given: two string s1 and s2,
        Ask: return True if s1 can be a permutation of substring of s2. e.g.
        Input: s1 = "ab" s2 = "eidbaooo"
        Output: True 
        because in s2 there is a substring 'ba' that is a permutation of 'ab'
        To accomplish this: idea here is to loop through s2 to check if there is a permutation of s1. 
        First, allocate both s1_count and s2_count lists to hold 26 zeros. The reason 26 is chosen
        is because we assume s1 and s2 only contain letters from a-z, and the trick here is to use 
        ord(letter) - ord('a'). ord() converts the given letter to its unicode number, e.g. ord('a') 
        is 97 and ord('b') is 98, but in order to make them start from 0 so as to fit in s1_count and s2_count, 
        we can do ord(letter) - ord('a'). 
        Next, loop s1 to record counts of each letter in s1 -> s1_count[ord(i)-ord('a')] += 1. here, letters in 
        s1 are converted to the index of s1_count and the value of a specific index is the counts of that letter
        in s1. e.g. if s1 = 'aba', s1_count = [2, 1] because ord('a') - ord('a') = 0, so s1_count[0] += 1 is 1, and 
        ord('b') - ord('a') = 1, so s1_count[1] += 1 is 1. then there is another 'a' so add another 1 to index 0 of
        s1_count and after looping s1 we have s1_count = [2, 1]
        we then loop s2 using same method. the catch here is when len(s2) > len(s1), image we have a cursor reading 
        s2 from left to right, all letters to the right of the cursor are what will be read and what's to the left of 
        the cursor is what has been read into s2_count. We need to control what's in s2_count so the total letters read 
        in s2 equals to the total letters in s1. Since we still have more on the right of the cursor to read, we need to 
        remove letters that we previously read: reading one more letter on the right, we need to remove one letter 
        from the left -> s2[i-s1_len]. i is the current cursor position by subtracting s1_len, we get that left letter 
        that should be removed from s2_count. 
        if s2_count equals s1_count: return True
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if s1 is longer than s2 then s1 can't be a substring of s2
        if len(s1) > len(s2):   return False
        s1_len = len(s1); s2_len = len(s2)
        # allocate two lists
        s1_count = [0] * 26; s2_count = [0] * 26
        for i in s1:
            s1_count[ord(i)-ord('a')] += 1
        for i in range(s2_len):
            s2_count[ord(s2[i])-ord('a')] += 1
            if i > s1_len-1:
                s2_count[ord(s2[i-s1_len])-ord('a')] -= 1
            if s2_count == s1_count:
                return True
        return False
            
        
