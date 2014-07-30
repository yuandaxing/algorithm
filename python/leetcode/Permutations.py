class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    # @ first A[i] for choose A[j] to A[i] then 
    def __init__(self) :
        self.res = []
    def permuteAux(self, num, i) :
        if i >= len(num) :
            self.res.append(list(num))
            return ;
        for j in range(i, len(num)) :
            num[i], num[j] = num[j], num[i]
            self.permuteAux(num, i+1)
            num[i], num[j] = num[j], num[i]
    def permute(self, num):
        self.permuteAux(num, 0)
        return self.res

num = [1,2,3]

sol = Solution()
print sol.permute(num)
            
        
