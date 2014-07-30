class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    # F[i][j]'s neighbour is F[i-1][j-1], F[i-1][j]
    # previous, current = [0 for i in range(len(triangle))], \
    #                     [0 for i in range(len(triangle))]
    # F[i][j] = max(MIN if j > i-1 F[i-1][j], MIN if j-1 < 0 \
    #      previous[j-1]) + triangle[i][j]
    def minimumTotal(self, triangle):
        MAXINT = 100000000
        previous, current = [ 0 for i in range(len(triangle))], \
                            [ 0 for i in range(len(triangle))]
        if len(triangle) == 0 :
            return 0
        previous[0] = triangle[0][0]
        for i in range(1, len(triangle)) :
            for j in range(len(triangle[i])) :
                current[j] = min(MAXINT if j > i-1 else previous[j], 
                                 MAXINT if j-1 < 0 else previous[j-1]) \
                    + triangle[i][j]
            previous, current = current, previous
        return min(previous)

test = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
sol = Solution()
print sol.minimumTotal(test)
