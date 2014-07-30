class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) == 0 : return ''
        commonPrefix = strs[0]
        for i in range(1, len(strs)) :
            commonIdx = 0
            while commonIdx < min(len(commonPrefix), \
                                       len(strs[i])) :
                if commonPrefix[commonIdx] != strs[i][commonIdx]:
                    break
                commonIdx += 1
            commonPrefix = commonPrefix[0:commonIdx] 
        return commonPrefix


sol = Solution()
tests = ['abcd', 'abc']
print sol.longestCommonPrefix(tests)
