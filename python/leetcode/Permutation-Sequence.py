class Solution:
    # @return a string
    def getPermutation(self, n, k):
        F = [1 for i in range(n)]
        for i in range(1, len(F)) :
            F[i] = i * F[i-1]
        num = [str(i) for i in range(1, n+1)]
        result = []
        for i in range(len(F)-1, -1, -1) :
            cur = k / F[i]
            k = k % F[i]
            result.append(num.pop(cur))
        return ''.join(result)


sol = Solution()
print sol.getPermutation(3, 1)
            
            
