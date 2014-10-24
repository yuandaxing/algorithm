#N = len(s3)
#memo = [False for i in s3]
#memo[0] = True
#for i in range(2, N+1, 2) :
#    z = i / 2
#    for j in range(1, z+1) :
#        if F[z-(j+1)*2] :
             # sub1 = s1[z-j:z]
             # sub2 = s1[z-j:z]
             # t = s3[i-j*2:i]
             # if sub1+sub2 == t or sub2+sub1==t :
             #     F[i] = True
             #     break
# F[m][n] = F[L][k] s1[L+1:m+1]+s2[k+1:n+1] == t[L+k+2:m+n+2]
# return F[len(s1)][len(s2)]

class Solution:
    # @return a boolean
    def isInterleave1(self, s1, s2, s3):
        N = len(s3)
        F = [False for i in range(len(s3)+1)]
        F[0] = True
        for i in range(2, N+1, 2) :
            z = i / 2
            for j in range(1, z+1) :
                if F[i-j*2] :
                    sub1 = s1[z-j:z]
                    sub2 = s2[z-j:z]
                    t = s3[i-j*2:i]
                    if sub1+sub2 == t or sub2+sub1 == t :
                        F[i] = True
                        break
        return F[N]

    def isInterleave2(self, s1, s2, s3):
        M, N = len(s1), len(s2)
        F = [[False for i in range(len(s2)+1)]
             for j in range(len(s1)+1)]
        F[0][0] = True
        for i in xrange(0, M+1) :
            for j in xrange(0, N+1) :
                for L in xrange(0, i+1) :
                    for K in xrange(0, j+1) :
                        if F[i-L][j-K] :
                            sub1 = s1[i-L:i]
                            sub2 = s2[j-K:j]
                            t = s3[i+j-(L+K) : i+j]
                            if sub1+sub2 == t or sub2+sub1 == t :
                                F[i][j] = True
                                break
        return F[M][N]

    def isInterleave(self, s1, s2, s3):
        M, N, H= len(s1), len(s2), len(s3)
        if M+N != H:
            return False
        F = [[False for i in range(len(s2)+1)]
             for j in range(len(s1)+1)]
        F[0][0] = True
        for i in range(0, M+1) :
            for j in range(0, N+1) :
                t = '' if i+j-1 < 0 else s3[i+j-1]
                if i-1 >= 0 and F[i-1][j] and s1[i-1] == t :
                    F[i][j] = True
                elif j-1 >= 0 and F[i][j-1] and s2[j-1] == t:
                    F[i][j] = True
        return F[M][N]




s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
s = Solution()
print s.isInterleave(s1, s2, s3)
