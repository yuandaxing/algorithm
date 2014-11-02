class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permutationAux(self, num, i) :
        if i == len(num) :
            return [tuple(num)]
        result = []
        for k in range(i, len(num)) :
            num[i], num[k] = num[k], num[i]
            result += self.permutationAux(num, i+1)
            num[i], num[k] = num[k], num[i]
        return result
    def permuteUnique(self, num):
        v = self.permutationAux(num, 0)
        return list(set(v))

s = [3,3,1,2,3,2,3,1]
sol = Solution()
print sol.permuteUnique(s)
