class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    # counting sort algorithm
    # Color = [0, 0, 0]
    # calcluate the counting
    # fill the array by counting
    def sortColors(self, A):
        color = [0, 0, 0]
        for e in A :
            color[e] += 1
        idx = 0
        for i in range(len(color)) :
            for j in range(color[i]) :
               A[idx], idx = i, idx+1

sol = Solution()
A = [0, 1, 0, 2, 1, 0, 1]
sol.sortColors(A)
print A 
