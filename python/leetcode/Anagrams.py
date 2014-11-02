class Solution:
    # @param strs, a list of strings
    # @return a list of strings
    def getKey(self, s) :
        cs = list(s)
        cs.sort()
        return ''.join(cs)
    def anagrams(self, strs):
        dicStr = {}
        for s in strs :
            key = self.getKey(s)
            dicStr.setdefault(key, [])
            dicStr[key].append(s)
        result = []
        for k, v in dicStr.iteritems() :
            if len(v) > 1 :
                result += v
        return result

s = ['ab', 'aa', 'ba', 'ac', 'ca']
sol = Solution()
print sol.anagrams(s)
