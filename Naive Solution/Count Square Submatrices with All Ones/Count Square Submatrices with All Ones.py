'''
    Runtime: 
        time: isSqure takes O(min(m-x, n-y)^2) since the two loops, countXY takes O(min(m, n)) since it increment length 
        by 1 each time until reach the termination condition. countSquares takes O(m*n) since two loops. Total takes
        O(m*n*min(m, n)*min(m-x, n-y)^2), simplify it to O(m^4)
        space: no extra space allocated to hold values, so O(1)
    Analysis:
        Given: a m * n matrix of ones and zeros
        Ask: how many squares submatrices have all ones
        Input: matrix =
        [
          [0,1,1,1],
          [1,1,1,1],
          [0,1,1,1]
        ]
        Output: 15
        To accomplish this: a square submatrix only satisfies the question by have all 1s in it, and if the current 
        matrix satifies the condition, we can add 1 to the length of this matrix and test if the expanded matrix 
        still satisfies the condition, if so we keep expanding, if not we return 0 and exit from this iteration. 
        With this logic, we can design isSquare function, and use countXY to exhaust all possible submatrices with 
        top left corner being (x, y). countSquares will loop all points in the given matrix.
'''

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                res += self.countXY(i, j, 0, matrix)
        return res
        
    def countXY(self, x, y, length, matrix):
        if x+length >= len(matrix) or y+length >= len(matrix[0]) or not self.isSquare(x, y, length, matrix):
            return 0
        return 1 + self.countXY(x, y, length+1, matrix)
    
    def isSquare(self, x, y, length, matrix):
        exp = (length+1) ** 2
        act = 0
        for r in range(x, x+length+1):
            for c in range(y, y+length+1):
                act += matrix[r][c]
        return act == exp
