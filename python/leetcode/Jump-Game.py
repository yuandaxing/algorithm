class Solution:
    # @param A, a list of integers
    # @return a boolean
    # B[0] = 1
    # for i in range(len(A)) :
    #   if B[i] == 1 :
    #     for j in range(A[i])
    #          if i+j+1 < len(A) :
    #          B[i+j+1] = 1
    def canJump(self, A):
        B = [0 for i in range(len(A))]
        if len(A) == 0 : return True
        prev, B[0] =0, 1
        for i in range(len(B)) :
            if B[i] and A[i] > prev :
                for j in range(A[i]) :
                    if i+j+1 < len(B) :
                        B[i+j+1] = 1
                prev = A[i]
            prev -= 1
        return B[len(A)-1]==1

sol = Solution()
print sol.canJump([2,3,1,1,4])
print sol.canJump([3,2,1,0,4])
