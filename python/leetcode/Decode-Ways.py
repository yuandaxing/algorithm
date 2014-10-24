class Solution:
    # @param s, a string
    # @return an integer
    def numDecodings(self, s):
        if not s : return 0
        F = [0 for i in range(len(s)+1)]
        F[0] = 1
        if len(s) > 0 :
            F[1] = 1
        for i in range(2, len(s)+1) :
            F[i] = F[i-1] if  int(s[i-1:i]) > 0 else 0
            if 10 < int(s[i-2:i]) <= 26 :
                F[i] += F[i-2]
        return F[len(s)]



S = '12'
sol = Solution()
print sol.numDecodings(S)
