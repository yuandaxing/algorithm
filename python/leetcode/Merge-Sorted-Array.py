class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    # merge from right to left
    def merge(self, A, m, B, n):
        idx3, idx1, idx2 = m+n-1, m-1, n-1
        while idx1 >= 0 or idx2 >= 0 :
            cur = 0
            if idx1 < 0 :
                cur, idx2 = B[idx2], idx2-1
            elif idx2 < 0 :
                break
            elif A[idx1] > B[idx2] :
                cur, idx1 = A[idx1], idx1-1
            else :
                cur, idx2 = B[idx2], idx2-1
            A[idx3], idx3 = cur, idx3-1


sol = Solution()
print sol.merge([1], 1, [], 0)
