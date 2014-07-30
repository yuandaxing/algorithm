class Solution:
    # @return an integer
    # dynamic programming
    # F[i][j] = F[i-1][j-1] + F[i-1][j] or F[i-1][j] i is the idx of S,
    # j is idx of T
    #  return F[len(s)-1][len(T)-1]
    
    def numDistinct(self, S, T):
        res = [[0 for j in range(len(T))] for i in range(len(S))]
        if len(S) >= len(T) and len(T) == 0 :
            return 1
        if len(S) == 0 : return 0
        for i in range(len(S)) :
            for j in range(len(T)) :
                Fi_1j_1= 1 if j==0 else (0 if i == 0 else res[i-1][j-1])
                Fi_1j = 0 if i < 1 else res[i-1][j]
                res[i][j] = Fi_1j + (Fi_1j_1 if S[i] == T[j] else 0)
        return res[len(S)-1][len(T)-1]
        
