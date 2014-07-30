class Solution:
    # @return an integer
    # N is the length
    # F[0][0] = 0 F[0][1] = 1, F[1][0] = 1
    # F[i][j] = { F[i-1][j] + 1, F[i][j-1] + 1, 
    # F[i-1][j-1] if word[i-1]==word2[j-1] else F[i-1][j-1]+1 }
    # F[0][k] = k F[k][0] = k
    def minDistance(self, word1, word2):
        F = [[0 for i in range(len(word2)+1)] for j in range(len(word1)+1)]
        for i in range(len(F)) : F[i][0] = i
        for i in range(len(F[0])) : F[0][i] = i
        for i in range(1, len(F)) :
            for j in range(1, len(F[i])) :
                F[i][j] = min(F[i-1][j]+1, F[i][j-1]+1, F[i-1][j-1]+1 if word1[i-1] != word2[j-1] \
                              else F[i-1][j-1])
        return F[len(word1)][len(word2)]


sol = Solution()
print sol.minDistance('', '')
