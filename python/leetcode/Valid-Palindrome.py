class Solution:
    # @param s, a string
    # @return a boolean
    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        while i < j :
            if not s[i].isalnum() :
                i += 1
            elif not s[j].isalnum() :
                j -= 1
            elif s[j].lower() == s[i].lower() :
                i, j = i+1, j-1
            else :
                break
        return i >= j

test = "A man, a plan, a canal: Panama"
sol = Solution()
print sol.isPalindrome(test)
