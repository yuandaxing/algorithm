class Solution:
    # @param s, a string
    # @return an integer
    # @ F[i] is the minmal cut for s[0....i]
    # @ F[i] = min{F[j]+1} if j+1...i is parlindrome
    # @ F[z] = 0 if z <0
    # @ O(N**2)
    def minCut(self, s):
        def isPar(i,j) :
            while i < j and s[i] == s[j] :
                i,j = i+1, j-1
            return i >= j
        parlindrome = [[False for i in range(len(s))] for j in range(len(s))]
        
        F = [10000 for i in range(len(s))]
        if not len(s): return 0
        for i in range(len(s)) :
            for j in range(i+1) :
                if s[i] == s[j] and (True if i-1<j+1 \
                                     else parlindrome[j+1][i-1]) :
                    F_j_1 = 0 if j-1 < 0 else F[j-1]
                    F[i] = min(F[i], F_j_1 + 1)
                    parlindrome[j][i] = True
        #for i in parlindrome :
        #    for j in i :
        #        print j,
        #    print ""
        return F[len(F)-1] - 1
    def minCut1(self, s):
        def isPar(i,j) :
            while i < j and s[i] == s[j] :
                i,j = i+1, j-1
            return i >= j
        F = [10000 for i in range(len(s))]
        if not len(s): return 0
        for i in range(len(s)) :
            for j in range(i+1) :
                if isPar(j, i) :
                    F_j_1 = 0 if j-1 < 0 else F[j-1]
                    F[i] = min(F[i], F_j_1+1)
        return F[len(F)-1]


sol = Solution()
print sol.minCut("aab")
print sol.minCut("abbab")
#print sol.minCut("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")


############################
#this is the most neat code for this 
#class Solution {
#public:
#    int minCut(string s) {
#        int N = s.size();
#        vector<int> dp(N+1,numeric_limits<int>::max());
#        dp[0] = 0;
#        for(int i=0;i<N;i++)
#        for(int p=0;p<=1;p++)
#        for(int l=0;l<=N;l++) {
#            int a=i-l, b = i+l+p;
#            if( a < 0 || b >= N || s[a]!=s[b] )
#                break;
#            dp[b+1] = min(dp[b+1],dp[a]+1);
#        }
#        return dp[N]-1;
#    }
#};
