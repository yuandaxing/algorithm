class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        res = [0 for i in range(rowIndex+1)]
        resSave = [0 for i in range(rowIndex+1)]
        for i in range(rowIndex+1) :
            for j in range(i+1) :
                if j == 0 or j == i :
                    res[j] = 1
                else :
                    res[j] = resSave[j-1]+resSave[j]
            res, resSave = resSave, res
        return resSave

sol = Solution()
print sol.getRow(3)
            
