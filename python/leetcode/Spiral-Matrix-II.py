class Solution:
    # @return a list of lists of integer
    # nSpirals = n / 2
    # cycle, elements = (cycle-1)*4
    # for i in range(nspirals) :
    #    cycle = n - 2 * i
    #    for j in range((cycle-1) * 2)
    #         if j >= 0 and j < cycle :
    #             idx = i, j % cycle
    #         elif  j < 2 * cycle - 1
    #             idx = j% cycle, n - i
    #         elif j < 3 * cycle -2 :
    #             idx = n - i, n - cycle % 3 - i
    #         else :
    #             idx = n-cycle % 3 - i, n-i
    def generateMatrix(self, n):
        res = [[0 for i in range(n)] for j in range(n)]
        nSpiral, element = (n+1) / 2, 1
        for i in range(nSpiral) :
            cycle = n - 2 * i
            nElement = (cycle - 1) * 4 if cycle > 1 else 1
            for j in range(nElement) :
                idx = None
                if j < cycle :
                    idx = i, i + j % cycle
                elif j < 2 * cycle - 1 :
                    idx = i + (j+1) % cycle, n - i - 1
                elif j < 3 * cycle - 2 :
                    idx = n - i - 1, n - (j + 2) % cycle - i - 1
                else :
                    idx = n - 1 - i - (j+3)%cycle, i
#                print idx
                res[idx[0]][idx[1]], element = element, element+1
        return res



sol = Solution()
print sol.generateMatrix(3)
