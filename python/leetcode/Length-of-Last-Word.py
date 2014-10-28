class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        v = s.split(' ')
        for e in v[-1::-1]:
            if e  :
                return len(e)

s = "Hello World"
sol = Solution()
print sol.lengthOfLastWord(s)

