class Solution:
    # @param n, an integer
    # @return an integer
    # F(1) = 1, F(0) = 1
    # F(2) = 1 + F(1) * F(1)
    # F(n) = F(n-1) + F(n-2)
    def climbStairs(self, n):
        FN, FN_1 = 1, 1
        for i in range(2, n+1) :
            FN, FN_1 = FN_1 + FN, FN
        return FN

test = 5
sol = Solution()
print sol.climbStairs(test)
