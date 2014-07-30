class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0 : return 0
        i,j,LEN = 0, 1, len(A)
        while j < LEN :
            if A[i] != A[j] :
                A[i], i = A[j], i+1
            j += 1
        return i+1
