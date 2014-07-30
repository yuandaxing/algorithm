class Solution:
    # @param prices, a list of integer
    # @return an integer

    # find the max S[j] - S[i] where j > i.
    def maxProfit(self, prices):
        minimal = [0 for i in range(len(prices))]
        maximal = [0 for i in range(len(prices))]
        preMin, preMax = 1000000, -1000000
        for i in range(len(prices)) :
            minimal[i] = min(preMin, prices[i])
            preMin = minimal[i]
        for i in range(len(prices)-1, -1, -1) :
            maximal[i] = max(preMax, prices[i])
            preMax = maximal[i]
        maxP = 0
        for i in range(len(prices)) :
            maxP = max(maxP, maximal[i] - minimal[i])

        return maxP

price = [1, 2,3,4,2,3,1]
sol = Solution()
print sol.maxProfit(price)
