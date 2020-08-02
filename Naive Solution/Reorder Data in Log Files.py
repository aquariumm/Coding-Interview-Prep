'''
    Rumtime:
        time: O(nlogn). 
        list comprehension takes O(n), n be the length of given list. sort takes O(nlogn), so total O(nlogn).
        In the list comprehension it calls a funtion that takes O(1) because it looks for the first occurence of 
        a space and that means the serach will continue for just the indentifiers' length, so amortized time 
        would be O(1). 
        space: O(n). list comprehension and sort all take O(n)
    Analysis: 
        Given: a list of logs
        Ask: return sorted list by lexicological order. The first word in each log is an identifier, so the sort should 
        focus on starting from the second word, only exception is when two logs have everything identical except for 
        identifiers, in which case sort by based on the identifers. For logs that start with number, keep order as they 
        appear in the given list, and append to the sorted list. e.g.
        Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
        Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
        To accomplish this: we can divide the problems into two parts, logs that are letter based and that are 
        number based. Number based, keep as is, letter based sort by lexicological order. To identify if letter based, 
        check the word after the first space, if letter then letter based, else not. apply sort on the letter based
        then append number based to the sorted letter based.
'''
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # check if empty
        if not logs:    return []
        # identify if this is a number based log
        def if_dig(s):
            pos = s.find(" ")
            return s[pos+1].isdigit()
        
        # divide the given logs
        dig = [_ for _ in logs if if_dig(_)]
        lett = [_ for _ in logs if not if_dig(_)]
        
        # sort the letter based
        lett.sort(key=lambda x: (x[x.find(" ")+1:], x[:x.find(" ")]))
        
        # append number based before return results
        return lett+dig
