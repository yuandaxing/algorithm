class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer

    def subset(self, eCount, i) :
        if i >= len(eCount) :
            return [[]]
        result = []
        for e in self.subset(eCount, i+1) :
            cur = list(e)
            cur.append(eCount[i])
            result.append(cur)
            result.append(e)
        return result 
        
    def subsets(self, S):
        S.sort()
        return map(lambda e : e[-1::-1], self.subset(S, 0))

S = [1,2,3]
sol = Solution()

print sol.subsets(S)
