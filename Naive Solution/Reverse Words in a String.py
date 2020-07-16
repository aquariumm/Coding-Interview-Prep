'''
    Runtime: 
        time: O(n), n is the number of words in s. becuase split() and the iteration take O(n) both
        space: O(n), extra space is needed when convert input to a list
    Analysis: 
        Given: a str that contains words
        Ask: reverse the given
        To accomplish this: first split the str to list, then iterater over the list from back to front. 
        join each element by a space.
'''
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i for i in s.split()[::-1]])
        
