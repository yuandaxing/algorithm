#Say you have an array for which the ith element is the price of a 
#given stock on day i.
#
#Design an algorithm to find the maximum profit. 
#You may complete at most two transactions.
class Solution:
    # @param prices, a list of integer
    # @return an integer
    # @ sigma(prices[j1]+prices[i1] - prices[j] - prices[i])
    #  where j1 > j and i1 > i where j1, i1, j and i are different number
    # 
    def maxProfitAux(self, prices):
        def TryToSell(i):
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
        i, sum, buySell = 0, 0, []
        while i < len(prices)-1 :
            j = TryToSell(i)
            if prices[j] > prices[i] :
                buySell.append(prices[j] - prices[i])
            i = j
        return sum, buySell
    def maxProfit(self, prices) :
        sum, buySell = self.maxProfitAux(prices) 
        buySell.sort()
        if len(buySell) == 0 :
            return 0
        elif len(buySell) == 1 :
            return buySell[0]
        else:
            return buySell[len(buySell)-1] + buySell[len(buySell)-2]
# F[i] = max(A[0:i]) - min(A[0:i])
# B[i] = max(A[i:len(b)]) - min(A[i:len(B)]
# for i in range(len(A)-1)
#     max = max(max, F[i]+B[i+1])
sol = Solution()
print sol.maxProfit([1,2])
