class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        B=[0 for i in range(len(A))]
        C=[0 for i in range(len(A))]
        if len(A) == 0 : return 0
        maxLeft, maxRight = A[0], A[len(A)-1]
        for i in range(len(A)) :
            B[i] = max(maxLeft, A[i])
            C[len(A)-1-i] = max(maxRight, A[len(A)-1-i])
            maxLeft, maxRight = B[i], C[len(A)-1-i]
#            print 'B[i]', B[i], 'C[i]',  C[len(A)-1-i]
        
        sumV = 0
        for i in range(len(A)) :
            sumV += min(B[i], C[i])-A[i]
        return sumV


sol = Solution()
print sol.trap([4,2,3])
