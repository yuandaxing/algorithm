class Solution:
    # @return a boolean
    def wildChar(self, s, i) :
        return (len(s)-i>1) and s[i+1]=='*'
    def isMatchA(self, s, si, p, pj) :
        if si >= len(s) or pj >= len(p) :
            return si >= len(s) and (pj >= len(p) 
                                     or (self.wildChar(p, pj)
                                         and pj == len(p)-2))
        
        if self.wildChar(p, pj) :
            if self.isMatchA(s, si, p, pj+2) :
                return True
            else :
                return (p[pj]=='.' or p[pj] == s[si]) and self.isMatchA(s, si+1, p, pj)
        else :
            return (p[pj]=='.' or p[pj]==s[si]) and self.isMatchA(s, si+1, p, pj+1)
    def isMatch(self, s, p):
        return self.isMatchA(s, 0, p, 0)


sol = Solution()
print sol.isMatch("aa","a")
print sol.isMatch("aa","aa")
print sol.isMatch("aaa","aa")
print sol.isMatch("aa", "a*") 
print sol.isMatch("aa", ".*")
print sol.isMatch("ab", ".*")
print sol.isMatch("aab", "c*a*b")
print sol.isMatch("aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c")
        
