'''
    Runtime: 
        time: if the time to loop each char in a word is significant, then time would be O(mn), m is the len of 
        words list, and n is the len of word. If len of word is negligible, then O(m).
        space: order_dict takes addtional space, so O(M)
    Analysis:
        Given: a words list, and an order str
        Ask: check if the list is arranged as per order
        Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
        Output: true
        To accomplish this: compare adjacent words in the list, if they all are in order then the list is in order
'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
    """Determine if words list is in order by the given order
    
    :words: a list of words
    :order: a given order in str
    :rtype: if words are in order
    """
        # construct order_dict that's needed by helper func
        order_dict = {string : i for i, string in enumerate(order)}
        # loop through each word in the dict, since i + 1 is used, loop till second last word in list
        for i in range(len(words) - 1):
            w1 = words[i]
            w2 = words[i + 1]
            # return False if adjacent words are out of order
            if not self.compareAdjacentTwoByOrder(w1, w2, order_dict):
                return False
        # given list is in order if its adjacent words are in order
        return True
    
    def compareAdjacentTwoByOrder(self, w1, w2, order_dict):
    """Helper function to validate adjacent words by the given order in a dict.
    
    :w1: first word
    :w2: second word
    :order_dict: order in a dict
    :rtype: bool to indicate if the two words are in order
    """
        # loop through each character in two words up to end of the shorter word
        for i in range(min(len(w1), len(w2))):
            if w1[i] != w2[i]:
                # when two chars aren't same, return if c1 is before c2 in the given dict
                return True if order_dict[w1[i]] < order_dict[w2[i]] else False
        # if reach here, it mean up to the end of the shorter word, chars in two words are same
        # but need to ensure w1 < w2 to aviod cases w1 = apply and w2 = app
        return True if len(w1) <= len(w2) else False
