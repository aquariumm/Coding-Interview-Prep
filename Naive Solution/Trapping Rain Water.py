'''
    Runtime:
        time: O(n). for two loop take O(n) each, n is the length of the given list, the max function inside takes 
        O(1) since only two elements are compared each time. The reverse() takes another O(n), and the list 
        comprehension takes O(n)
        space: O(n). l_height, r_height and delta take O(n) each. 
    Analysis: 
        Given: a list of heights 
        Ask: calculate how many units of water can be trapped in the given list
        Input: [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6
        To accomplish this: we can find out how much water can be trapped at each height in the given list, and 
        sum them up to get the total. The water trapped at each height can be determined by 3 factors, the max 
        height (l_height) to the left of the current height, the current height, and the max height (r_height) 
        to the right of the current height. The only time that water can be trapped is when both l_height and 
        r_height is taller than the current height, calculate the height difference between l_height and height, 
        and r_height and height, and the shorter difference is how much water can be trapped. 
        to calculate how many units of water will be trapped in each height
'''
class Solution:
    def trap(self, height: List[int]) -> int:
        # check if empty
        if not height: return 0
        
        # set vars
        LENGTH = len(height)
        
        # construct lists for left and right heightest
        l_height = [height[0]]
        r_height = [height[LENGTH-1]]
        
        # add elements to lists
        for i in range(1, LENGTH):
            l_height.append(max(l_height[i-1], height[i]))
        for i in range(1, LENGTH):
            r_height.append(max(r_height[i-1], height[LENGTH-i]))
        print(r_height)
        r_height.reverse()
        
        # calculate delta in each position
        delta = [min(l_height[i] - height[i], max(0, r_height[i] - height[i])) for i in range(LENGTH-1)]
        
        # return results
        return sum(delta)
