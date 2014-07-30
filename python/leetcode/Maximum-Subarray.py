class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        if len(A) == 0 :
            return 0
        curMax, globalMax = A[0], A[0]
        for i in range(1, len(A)) :
            curMax = A[i] + max(0, curMax)
            globalMax = max(curMax, globalMax)
        return globalMax

sol = Solution()
print sol.maxSubArray([−2,1,−3,4,−1,2,1])
