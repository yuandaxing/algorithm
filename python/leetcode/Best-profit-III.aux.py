class Solution:
    # @param prices, a list of integer
    # @return an integer
    # min is minmal A[0:i]
    # max is maximum A[i:len]
    # if i the seperation  max(A[j] - A[j1] + B[k] - A[k-1]) where j, j1 <=i
    # and j > j1 and k, k1 > i and k > k1
    # B[i] = (A[i] - min) where min = A[i1] i1 <= i
    # C[i] = (max - A[i]) where max = A[i1] i1 > i
    # 
    def maxProfit(self, prices):
        B=[0 for i in range(len(prices))]
        C=[0 for i in range(len(prices))]
#        print len(prices) <= 1
        if len(prices) <= 1 :
            return 0
        minF, maxB = prices[0], prices[len(prices)-1]
        for i in range(len(prices)) :
            minF = min(minF, prices[i])
            B[i] = prices[i] - minF
            maxB = max(maxB, prices[len(prices)-i-1])
            C[len(prices)-i-1] = maxB - prices[len(prices)-i-1]
        maxF, maxB = B[0], C[len(C)-1]
        for i in range(len(B)) :
            B[i] = max(maxF, B[i])
            C[len(C)-i-1] = max(maxB, C[len(C)-i-1])
            maxF, maxB = B[i], C[len(C)-i-1]
        maxR = 0
        for i in range(0, len(prices)) :
            maxR = max(maxR, (0 if i-1<0 else B[i-1])+C[i])
        return maxR

sol = Solution()
print sol.maxProfit([1, 2])
