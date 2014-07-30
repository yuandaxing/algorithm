class Solution:
    # @return a list of lists of integers
    def collectCombin(self, n, start, k, res, cur) :
        if k == 0 :
            res.append(list(cur))
            return 
        elif start > n :
            return 
        else :
            self.collectCombin(n, start+1, k, res, cur) 
            cur.append(start)
            self.collectCombin(n, start+1, k-1, res, cur)
            cur.pop()
    def combine(self, n, k):
        res, cur = [], []
        self.collectCombin(n, 1, k, res, cur)
        return res


sol = Solution()
print sol.combine(4, 2)
        
