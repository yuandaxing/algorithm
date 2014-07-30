class Solution:
    # @param prices, a list of integer
    # @return an integer
    # sigma(A[j] - A[i]) j > i
    # max(sigma(A[j] - A[i]))
    # 
    def maxProfit(self, prices):
        def TryToSell(i) :
            j, acced = i, True if i >= len(prices)-1 else \
                       prices[i+1] >= prices[i]
            for j in range(i+1, len(prices)) :
                if prices[j] >= prices[j-1] and acced : 
                    continue 
                elif prices[j] < prices[j-1] and  not acced :
                    continue
                else :
                    return j-1
            return j
        i, sum = 0, 0
        while i < len(prices)-1 :
            j = TryToSell(i)
            sum += max(prices[j] - prices[i], 0)
            i = j
        return sum

sol = Solution()
print sol.maxProfit([1])
