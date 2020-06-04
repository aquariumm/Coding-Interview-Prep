'''
    Runtime:
        time: loop take O(n/2), n is the length of s
        space: O(1) because no extra space is needed
    Analysis: 
        Given: a list of str
        Ask: return the list in reverse order
        Input: ["h","e","l","l","o"]
        Output: ["o","l","l","e","h"]
        To accomplish this: imagine we scan the list from left and right at the same time
        by swapping the left str and right str and continue doing so until left and right meet, 
        we will have a reversed list. Specifically, we can have two pointers, left and right. left start
        from index 0 and right start from index len(n) -1. while left < right, it means the two pointers 
        have not met, so we need to continue scanning. 
'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0; right = len(s) -1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1; right -= 1
            
