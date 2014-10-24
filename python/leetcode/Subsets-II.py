class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def collectCounts(self, s) :
        d = {}
        for e in s:
            d.setdefault(e, 0)
            d[e] += 1
        result =  list(d.items())
        result.sort(key = lambda e: e[0])
        return result 
     def subset(self, eCount, i) :
        if i >= len(eCount) :
            return [[]]
        result = []
        for e in self.subset(eCount, i+1) :
            for k in range(eCount[i][1]+1) :
                cur = [eCount[i][0] for j in range(k)]
                cur.extend(e)
                result.append(cur)
        return result 
        
    def subsetsWithDup(self, S):
        d = self.collectCounts(S)
        return self.subset(d, 0)

S = [1,2,2]
sol = Solution()
print sol.subsetsWithDup(S)
