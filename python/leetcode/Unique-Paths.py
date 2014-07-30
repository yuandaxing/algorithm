class Solution:
    # @return an integer
    def numFac(self, n):
        res = 1
        for i in range(1, n+1):
            res *= i
        return res
    def uniquePaths(self, m, n):
        return self.numFac(m+n)/(self.numFac(m) * self.numFac(n))
    
sol = Solution()
print sol.uniquePaths(1,2)
