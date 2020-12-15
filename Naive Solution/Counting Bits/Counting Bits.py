'''
    Runtime: 
        time: the for loop takes O(n). Other operations take O(1). so total O(n)
        space: res is allocated to hold total of num items, so O(n)
    Analysis:
        Given: a non negative integer num
        Ask: return a list of numbers represents number of 1's in each value between [0, num] when in binary format
        Input: 2
        Output: [0,1,1]
        To accomplish this: loop through num, when a number is a power of 2, it only has ONE 1 in binary format, and 
        all other numbers between this number and the next number that is a power of two can all be composed 
        by sum of (this number and another value). With this, we can design `res` in such a way that
        list index represents the number and value in that index represent the number of 1's in binary format. 
        e.g. res[1] the 1 here represents the number 1 and we thus want the value
        held in that index to be the number of 1's for that number so we need to design it in a way 
        that res[1]=1 and so on)

'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0, 1]
        if num < 2:
            if num == 0:
                res.pop()
            return res
        
        mark = 0
        for i in range(2, num+1):
            if (i & (i-1)) == 0:
                # check if i is a power of 2
                mark = i
                res.append(1)
            else:
                res.append(res[i-mark] + 1)
                
        return res
        
    
