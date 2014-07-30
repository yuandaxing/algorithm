class Solution:
    def CanBreak(self, s, dict) :
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
    # @param s, a string
    # @param dict, a set of string
    # @return a list of strings
    def wordBreak(self, s, dict):
        def wordBreakAux(str) :
            result = []
            if str == '' :
                return ['']
            strLen = len(str)
            for i in range(1, strLen+1) :
                piece = str[0:i]
                if piece in dict :
                    res = wordBreakAux(str[i:strLen]) 
                    if res :
                        for r in res :
                            result.append(piece+' '+r)

            return result
        if self.CanBreak(s, dict) :
            return [str.strip() for str in wordBreakAux(s)]
        return []





test = "leetcode"

dict = set(["leet", "code"])
sol = Solution()
print sol.wordBreak("", dict)
print sol.wordBreak("leet", dict)
print sol.wordBreak(test, dict)
            

#ronnie672317781
