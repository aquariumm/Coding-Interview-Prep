'''
    Rumtime: 
        time: the while loop takes min(O(M), O(N)), M and N are the lengths of A and B. To set value at index
        i or j take O(1). result.append takes O(1). Total O(min(M, N))
        space: a list of result is allocated takes O(M+N)
    Analysis:
        Given: two lists of int: A and B 
        Ask: intersection of A and B. e.g.
        Input: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
        Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
        To accomplish this: we can iterate A and B, starting from first lists in them and stopping when one
        of them is looped entirely. for each iteration, we set a candidate, its interval starts at max(a1, b1)
        and stops at min(a2, b2), a1, a2 are the interval of A in this interation. i.e. A[i] is [a1, a2].
        and b1, b2 correspond to the start and end of B[j]'s interval. To understand why canadidate starts from 
        max(a1, b1) and stops at min(a2, b2), drwa a graph that two intervals overlap each other and 
        in order to get the intersection of the overlapped area, max and min have to be used. There will be 
        cases where the starting of one interval is bigger than the end of another interval, which is an invalid
        case that implies the two intervals have no overlapped area, and in such case, a check is performed:
        candidate[0] > candidate[1]. when candidate[0] > candidate[1] is true, we need to figure out which 
        interval has the smaller values, and that can be done through if candidate[1] == B[j][1]. if true, it
        mean B has the smaller interval and we need to move to B's next interval but remain A in its current 
        interval, and same rule applies to A. 
        When we have a valid candidate, we append it to result first and then check if the upper bound of 
        candidate is also the upper bound of both A and B, if so, we can safely add 1 to i and j to move to 
        their next intervals. However, if the upper bound of candidate is smaller than either A or B, we need 
        to reconstruct A or B, depending on which one has bigger upper bound than candidate. The reconstructed A 
        or B will stay in its current interval but the lower bound should be adjusted to the upper bound of 
        candidate.        
'''
class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # directly return if either A or B is empty
        if not A or not B:  return 
        # allocate result. i and j is for looping A and B
        i = 0; j = 0; result = []
        while i < len(A) and j < len(B):
            candidate = [max(A[i][0], B[j][0]), min(A[i][1], B[j][1])]
            if candidate[0] > candidate[1]:
                if candidate[1] == B[j][1]:
                    j+=1
                else:
                    i+=1
            else:
                result.append(candidate)
                if candidate[1] < A[i][1]:
                   
                    A[i]=[candidate[1], A[i][1]]
                    j+=1
                elif candidate[1] < B[j][1]:
                   
                    B[j]=[candidate[1], B[j][1]]
                    i+=1
                else:
                    i+=1; j+=1
        return result
        
