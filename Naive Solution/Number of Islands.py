'''
    Runtime: 
        time: O(n), n is the size of the given grid. Theoretically, the traverse loop takes O(n), and 
        in each iteration could call the recursive function, which also takes O(n), but the recursive funtion
        marks all its visited point so there is points that are visited by previous recursive calls will not 
        be visited again when the iteration comes to that point. Thus, O(n) is the total time
        space: depending on the given grid, if it is filled with 1s then the recursive stack will be significant, 
        which takes O(n). Else, O(1)
    Analysis:
        Given: a gird of 0s and 1s
        Ask: given a rule that if 1s are adjacent to each other, theis collection is considered as one iterm, 
        and if 1 is isolated and only surrounded by 0s, it is considered as another item, return how many items
        there are in the given grid. e.g. 
        Input: grid = [
          ["1","1","1","1","0"],
          ["1","1","0","1","0"],
          ["1","1","0","0","0"],
          ["0","0","0","0","0"]
        ]
        Output: 1
        To accomplish this: we only need to focus on 1s in the grid, and there are two cases: if it is isolated, 
        it is considered as one item, and if it is adjacent to other 1s, other 1s and this 1 should be considered 
        as a whole and count as one item.
        Once they are visited, they need to be marked in a way so they will not be visited again. isolated 1 
        is easy, only itself needs to be marked after visit. For adjacent 1s, they can be visited through a recursive
        call. Since it is a gird, the number of adjacent points to the current point can be 4 at most, they are one 
        position up, down, left, right. And we should remove points that are beyond grid boundary. 
'''
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if empty return 0
        if len(grid) == 0:  return 0
        # set vars
        # 4 directions that need to be traversed
        DIRECT = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        # row and col lenght
        ROW_LEN = len(grid); COL_LEN = len(grid[0])
        # counter
        counter = 0
        
        # helper function to mark adjacent 1s to 2, i being the current row position, j be the current col position
        def check_adj(i, j):
            if grid[i][j] in ('2', '0') :
                return 
            dirc = [[sum(_) for _ in zip(d, [i, j])] for d in DIRECT]
            
            # filter out over boundary points and points that are 2 or 0
            fil_dic = [d for d in dirc if not 
                       (d[0] < 0 or d[1] < 0 or d[0] >= ROW_LEN or d[1] >= COL_LEN 
                       
                       )]
            # mark 1 to 2 to indicate this point has been visited
            # grid[dir[0]][dir[1]] = '2'
            grid[i][j] = '2'
            for dir in fil_dic:
                # mark adjacent points
                check_adj(dir[0], dir[1])
        
        # traverse the matrix
        for i in range(ROW_LEN):
            for j in range(COL_LEN):
                if grid[i][j] == '1':
                    counter += 1
                    check_adj(i, j)
                    
        return counter
            
        
