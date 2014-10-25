class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        elements = path.split(r'/')
        v = []
        for e in elements :
            if e in ['', '.'] :
                continue 
            elif e == '..' :
                if v :
                    v.pop()
            else :
                v.append(e) 
        return '/'+('/'.join(v))

s1 = '/home/'
sol = Solution()
print sol.simplifyPath(s1)
