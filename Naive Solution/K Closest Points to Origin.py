'''
    Runtime: 
        time: construct the dict takes O(n), n being the lenth of the points List of List. sort the 
        dict takes O(nlogn) and the append operation inside take O(1). Total take O(nlogn)
        space: allocate a dict take O(n), allocate res takes O(n). so total O(n)
    Analysis:
        Given: a list of points. this list contains int only
        Ask: return points from the list, the order is from closed to the origin. total number of 
        points returned is equal to K
        Input: points = [[1,3],[-2,2]], K = 1
        Output: [[-2,2]]
        To accomplish this: we can choose dict to keep track of points in the list and their 
        distances to the origin. dict.keys being each point, and dic.values being the distance.
        then sort the dict based on element's values. One thing to notice is we have a count variable. It 
        is used for situations where K is less than the total number of elements in the dict. For K, there are 
        two cases, one is K == len(constructed dict), and one is K < len(contructed dict). If 
        K == len(constructed dict), we can safely return after iteration the sorted dict, and return res. 
        For cases when K < len(constructed dict), we need to return the results of res when count == K. 
'''

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # check if empty list 
        if not points:    return
        tem = defaultdict(int)
        for i in points:
            tem[tuple(i)] = math.sqrt(i[0]**2+i[1]**2)
        count = 1; res=[]
        for i in sorted(tem,key=tem.get):
            # cases when K is < len(tem)
            if count > K:
                return res
            else:
                res.append(list(i))
                count+=1
        return res
