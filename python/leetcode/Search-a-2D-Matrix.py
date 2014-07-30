class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    # @ i,j = 0, len(matrix[0])
    #  while i < len(matrix) and j >= 0
    #     v = matrix[i][j]
    #     if v == target : return True
    #     elif v < target : j -= 1
    #     else : i += 1
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0 : return False
        i, j = 0, len(matrix[0]) - 1
        while i < len(matrix) and j >= 0 :
#            print i, j
            v = matrix[i][j]
            if v == target : return True
            elif v > target : j -= 1
            else : i += 1
#            print i, j
        return False

sol  = Solution()
print sol.searchMatrix([[1,3]], 1)
        
