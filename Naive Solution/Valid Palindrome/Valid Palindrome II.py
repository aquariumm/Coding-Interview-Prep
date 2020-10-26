'''
    Rumtime:
        time: O(n), n is the lenght of s. The loop in validPalindrome takes half of len(s) if all chars are the same. 
        if there is a difference, then there is a substring of s[i: len(s) - i] not checked. Meanwhile, func
        validStrictPalindrome is called, and the unchecked substring is checked by it, and in this case, the run time is 
        also O(n) because the two funcs take two substring that constitutes the whole str.
        space: O(1) since no additonal space needed.
    Analysis:
        Given: a non-empty string s
        Ask: check if s is a palindrome when at most one character can be removed
        Input: "aba"
        Output: True
        To accomplish this: image two pointers from beginning and end of str, converging to the middle. If in this 
        process, all chars the same, then this is a palindrome with no need of removing a char. If there is a difference,
        check if by shift one char to the right or left can make it a palindrome.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        """validate if given s is a palindrome by given definition
        
        :s: given str
        :rtype: bool to indicate if s is a palindrome by given definition
        """
        # loop from first to the middle of the str, this is enough as the seconf half after mid 
        # is validated with the first half, note the use of tidle(~) operator
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                # if char not same, check if by shift one char to left or right will make a palindrome
                return self.validStrictPalindrome(s[i : ~i]) or self.validStrictPalindrome(s[i+1 : len(s) - i])
        return True
        
    def validStrictPalindrome(self, s):
        """Helper function to validate if the given str is a strict palindrome, so no skipping char allowed

        :s: given str to be validated
        :rtype: bool to indicate if s is a strict palindrome
        """
        for i in range(len(s)//2):
            if s[i] != s[~i]:
                return False
        return True
