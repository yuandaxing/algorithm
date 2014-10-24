def validIP(ip) :
    for e in ip :
        if int(e) > 255 :
            return False
        if len(e) > 1 and e.startwith('0'): 
            return False 

    return True
class Solution:
    # @param s, a string
    # @return a list of strings
    def permutation(self, s, m) :
        if m >= 4 :
            return [] if s else [[]]
        result = []
        for i in range(1, min(4, len(s)+1)) :
            for ele in self.permutation(s[i:], m+1) :
                ele.append(s[0:i])
                result.append(ele)
        return result
    def restoreIpAddresses(self, s):
        result = self.permutation(s, 0)
        result = map(lambda e : e[-1::-1], result)
        result = filter(validIP, result)
        return map(lambda e: '.'.join(e), result)


s = '25525511135'
sol = Solution()
print sol.restoreIpAddresses(s)
