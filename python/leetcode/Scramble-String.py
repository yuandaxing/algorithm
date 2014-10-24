class Solution:
    # @return a boolean
    def isScramble(self, s1, s2):
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

s1, s2 = 'great', 'rgtae'
sol = Solution()
print sol.isScramble(s1, s2)
