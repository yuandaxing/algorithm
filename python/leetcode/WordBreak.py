class Solution:
    # @param s, a string
    # @param dict, a set of string
    # @return a boolean

    def wordBreak1(self, s, dict):
        maxLen = max([len(str) for str in dict]) if dict else 0
        minLen = min([len(str) for str in dict]) if dict else 0
        if len(s) == 0 :
            return True
        start = min(maxLen, len(s))
        end = minLen-1
        for i in range(start, end, -1) :
            first = s[0:i]
            if first in dict :
                next = s[i:]
                if self.wordBreak(next, dict):
                    return True
        return False

    def wordBreak(self, s, dict) :
        maxLen = max([len(str) for str in dict]) if dict else 0
        minLen = min([len(str) for str in dict]) if dict else 0
        result = [False for i in range(0, len(s) + 1)]
        result[0] = True

        for i in range(1, len(s)+1) :
            for j in range(minLen, maxLen+1):
                if i - j  < 0 :
                    break
                else :
                    piece = s[i-j : i]
                    if result[i-j] and (piece in dict) :
                        result[i] = True
                        break
        return result[len(s)]
                    
            

test = "leetcode"

dict = set(["leet", "code"])
sol = Solution()
print sol.wordBreak("", dict)
print sol.wordBreak("leet", dict)
print sol.wordBreak(test, dict)
