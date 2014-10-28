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
    def Aux(self, sWeight, i, left) :
        if left == 0 :
            return [[]]
        if i >= len(sWeight) or left < sWeight[i][0] :
            return []
        result = []
        for k in range(sWeight[i][1]+1) :
            for sub in self.Aux(sWeight, i+1, left - k*sWeight[i][0]) :
                cur = list(sub)
                cur += [sWeight[i][0]] * k
                result.append(cur)
        return result

    def subSet(self, S, n) :
        v = self.collectCounts(S)
        sets = self.Aux(v, 0, n)
        sets = map(lambda e : e[-1::-1], sets)
        return sets


sets = [1,1,2,2,4,5,7,6]
s = Solution()
print s.subSet(sets, 7)
