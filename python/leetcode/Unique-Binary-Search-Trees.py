class Solution:
    # @return an integer
    # T(1) = 1
    # T(3) = T(2)+T(1)+T(2)
    # T(n) = T(n-1) + T(1)*T(n-2)+T(2)*T(n-3)+T(3)*T(n-4)+T(n-1)
    def numFac(self, n):
        res = 1
        for i in range(1, n+1):
            res *= i
        return res
    def numTrees(self, n):
        return self.numFac(2*n) / (self.numFac(n) * self.numFac(n) * (n+1))

test = 3
sol = Solution()
print sol.numTrees(test)
