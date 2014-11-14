class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def aux(self, candidates, target, i) :
        if target == 0:
            return [[]]
        if i >= len(candidates) or target < candidates[i] :
            return []
        result = []
        for k in range(target/candidates[i]+1) :
            for ele in self.aux(candidates, target - k * candidates[i], i+1) :
                cur = ele + [candidates[i]] * k
                result.append(cur)
        return result
    def combinationSum(self, candidates, target):
        candidates.sort()
        v = self.aux(candidates, target, 0)
        v = map(lambda e: e[-1::-1], v)
        return v


v = [2,3,6,7]
sol = Solution()
print sol.combinationSum(v, 7)
