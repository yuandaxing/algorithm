class Solution:
    # @return a list of lists of integers
    # S[i][j] if j == 0 or j == i
    # S[i][j] = S[i-1][j-1]+S[i-1][j]
    def generate(self, numRows):
        res = []
        for i in range(numRows) :
            cur = []
            for j in range(i+1) :
                if j == 0 or j == i :
                    cur.append(1)
                else :
                    cur.append(res[i-1][j-1]+res[i-1][j])
            res.append(cur)
        return res

    def printTri(self, res) :
        for cur in res:
            for i in cur:
                print i, '\t'
            print '\n'

sol = Solution()
res = sol.generate(5) 
sol.printTri(res)
