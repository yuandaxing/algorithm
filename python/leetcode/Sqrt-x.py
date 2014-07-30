class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        left, right = 0, x
        while left <= right :
            mid = (left+right) / 2
            r = mid * mid
            if r == x : return mid
            elif r < x : left = mid+1
            else : right = mid - 1
        return right


test = 13
sol = Solution()
print sol.sqrt(test)
