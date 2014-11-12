class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        if not A : return 0
        maxV, minV, maxG = A[0], A[0], A[0]
        for z in A[1:] :
            maxV, minV = max(maxV * z, minV * z, z), min(maxV * z, minV * z, z)
            maxG = max(maxG, maxV)

        return maxG

A = [2,3,-2,4]
s = Solution()
print s.maxProduct(A)
B = [-2]
C=[-4,-3,-2]
print s.maxProduct(C)
