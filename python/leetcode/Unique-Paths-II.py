class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    # [[0 for j in range(len(obstacleGrid[i]))]
    #     for i in range(len(obstacleGrid))]
    # F[i][j] = F[i-1][j] + F[i][j-1], F[i][j] if i <0 or j < 0 or 
    def uniquePathsWithObstacles(self, obstacleGrid):
        res = [[0 for j in range(len(obstacleGrid[i]))]
               for i in range(len(obstacleGrid))]
        for i in range(len(obstacleGrid)) :
            for j in range(len(obstacleGrid[i])) :
                if not i and not j and not obstacleGrid[0][0]: res[0][0] = 1; continue
                if not obstacleGrid[i][j] : 
                    res[i][j] = (0 if i-1<0 else res[i-1][j])+\
                                (0 if j-1<0 else res[i][j-1])

#        for i in range(len(obstacleGrid)) :
#            for j in range(len(obstacleGrid[0])) :
#                print res[i][j]
        return res[len(obstacleGrid)-1][len(obstacleGrid[0])-1]

ob = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
sol = Solution()
print sol.uniquePathsWithObstacles(ob)
