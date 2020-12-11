'''
    Runtime:
        time: the helper function takes O((2K)^2) as we can think of it as summing each point under an area, of which 
        height and width are both K. There is another nested loop that iterates each point in the mat, so total 
        is O(m*n*(2K)^2), m, n is the size of mat
        space: res, and local are created, so O(m*n)
    Analysis:
        given: m * n matrix, an integer K
        ask: compose a new matrix of which [i][j] is the sum of all elements mat[r][c] for 
        i - K <= r <= i + K, j - K <= c <= j + K
        Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
        Output: [[12,21,16],[27,45,33],[24,39,28]]
        To accomplish this: iterate each point in the given matrix and calculate sum of all points in the areas centered 
        at point[i][j] with length and width both of 2K.
'''

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        res = []
        for i in range(len(mat)):
            local = []
            for j in range(len(mat[0])):
                rowRange = [i-K if i-K >= 0 else 0, i+K+1 if i+K+1 <= len(mat) else len(mat)]
                colRange = [j-K if j-K >= 0 else 0, j+K+1 if j+K+1 <= len(mat[0]) else len(mat[0])]
                local.append(self.helper(i, j, rowRange, colRange, mat))
            res.append(local)
        return res
    
    def helper(self, i, j, rowRange, colRange, mat):
        res = 0
        for r in range(rowRange[0], rowRange[1]):
            for c in range(colRange[0], colRange[1]):
                res += mat[r][c]
        return res
