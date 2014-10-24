class Solution:
    # @return a boolean
    def isScramble1(self, s1, s2):
        F = [False for i in range(len(s2)+1)]
        F[0] = True
        for i in range(1, len(F)) :
            for k in range(1, i+1) :
                if F[i-k] :
                    cur, t = s1[i-k:i], s2[i-k:i]
                    if t == cur or t == cur[-1::-1] :
                        F[i] = True
                        break
        return F[len(s1)]

    # @return a boolean
    def isScramble(self, s1, s2):
        N = len(s1)
        F = [[[False for i in range(N+1)]
              for j in range(N)]
             for k in range(N)]
        for k in range(1, N+1) :
            for i in range(N-k+1) :
                for j in range(N-k+1) :
                    if k == 1 :
                        if s1[i] == s2[j] :
                            F[i][j][k] = True
                    else :
                        for L in range(1, k) :
                            if (F[i][j][L] and F[i+L][j+L][k-L]) or \
                               (F[i][j+k-L][L] and F[i+L][j][k-L]) :
                                F[i][j][k] = True
                                break
        return F[0][0][N] 
             

s1, s2 = 'great', 'rgtae'
sol = Solution()
print sol.isScramble(s1, s2)
