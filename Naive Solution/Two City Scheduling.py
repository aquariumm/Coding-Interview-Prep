'''
    Runtime: 
        time: sort() takes O(nlogn). loop takes O(n), sum() takes O(n). so total is O(nlogn)
        space: a, b use extra spaces. Each takes O(n/2). 
    Analysis:
        Given: a list of integers lists, the length is an even number. the structure is [[a1, b1], [a2, b2]]
        Ask: each integer list has two values e.g. a1, b1, for each of such integer list only 
        one of the values (so a1 or b1) can be selected, find a way to minimize the sum of selected a and b.
        also, number of selected a should equal to number of selected b.
        Input: [[10,20],[30,200],[400,50],[30,20]]
        Output: 110
        To accomplish this: sort the given list in descending order, such that larger difference between 
        a1 and b1 are listed first. then allocate two empty lists. for each integers list within 
        the given list, if positon 0 is smaller then add it to list a, else add to list b. 
        continue this until either a.length or b.length reaches half of cost.length, 
        Lets say if a.length == costs.length/2, so a is full, then all remaining lists in the given 
        list will have only one choice, get their b value put them to list b because list a has no more spaces.
'''

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key=lambda x: abs(x[1]-x[0]), reverse=True)
        a = []
        b = []
        for i in range(len(costs)):
            if len(a) == len(costs)/2:
                return sum(a+b, sum([j[1] for j in costs[i:]]))
            elif len(b) == len(costs)/2:
                return sum(a+b, sum([j[0] for j in costs[i:]]))
            else:
                if costs[i][0]<costs[i][1]:
                    a.append(costs[i][0])
                else:
                    b.append(costs[i][1])
            
