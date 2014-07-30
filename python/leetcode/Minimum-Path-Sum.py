class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    # @ define a grid contians tuple
    # @ init the first and second column
    # S[i][j][0] = min(S[i-1][j], S[i][j-1])+grid[i][j]
    # S[i][j][1] = arg{min(S[i-1][j], S[i][j-1])}
    def minPathSum(self, grid):
        MAX_INT = 1000000
        res = [[[0,0] for j in range(len(grid[i]))] for i in range(len(grid))]
        for i in range(len(grid)) :
            for j in range(len(grid[i])) :
                if not i and not j : res[0][0] = [grid[0][0], (0,0)]; continue;
                pos1, pos2 = (i-1, j), (i, j-1)
                v1, v2 = MAX_INT if i-1 < 0 else res[i-1][j][0], \
                         MAX_INT if j-1 < 0 else res[i][j-1][0]
                res[i][j] = [v2+grid[i][j], pos2] \
                            if v2 < v1 else [v1+grid[i][j], pos1]
        i, j = len(grid)-1, len(grid[0])-1

#        for i in range(len(res)) :
#            for j in range(len(res[i])) :
#                print res[i][j][0], '\t'
        return res[i][j][0]


grid = [[1,2],[1,1]]
sol = Solution()
print sol.minPathSum(grid)
