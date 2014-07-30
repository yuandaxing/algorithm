class Solution:
    # @param x, a float
    # @param n, a integer
    # @return a float
    def pow(self, x, n):
        n, sign = abs(n), (n >= 0)
        res, xn = 1, x
        while n :
            res *= xn if n % 2 else 1
            n = n / 2
            xn *= xn
        return res if sign else 1.0 / res

sol = Solution()
print sol.pow(2.5, 3)
