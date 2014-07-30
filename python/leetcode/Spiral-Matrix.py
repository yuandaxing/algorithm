class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        res = []
        if not len(matrix) :
            return res
        m, n = len(matrix), len(matrix[0])
        z = min(m, n)
        nSpiral = (z+1) / 2

        for i in range(nSpiral) :
            nElement = (n+m-4*i)*2-4 if min(m,n)-2*i>=2 else max(m,n)-2*i
            #print "nElment", nElement
            for j in range(nElement) :
                idx, mcycle, ncycle = None, m - 2 * i, n - 2 * i
                if j < ncycle:
                    idx = i, i + j 
                elif j < mcycle + ncycle - 1 :
                    idx = i + (j+1 - ncycle) , n - i - 1
                elif j < 2*ncycle+mcycle-2:
                    idx = m - i - 1, n - (j + 2 - ncycle - mcycle)  - i - 1
                else :
                    idx = m - 1 - i - (j-2*ncycle-mcycle+3), i
                #print idx
                res.append(matrix[idx[0]][idx[1]])
        return res

test = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

sol = Solution()
print sol.spiralOrder(test)

print sol.spiralOrder([[6,9,7]])
print sol.spiralOrder([[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30],[31,32,33,34,35,36,37,38,39,40],[41,42,43,44,45,46,47,48,49,50],[51,52,53,54,55,56,57,58,59,60],[61,62,63,64,65,66,67,68,69,70],[71,72,73,74,75,76,77,78,79,80],[81,82,83,84,85,86,87,88,89,90],[91,92,93,94,95,96,97,98,99,100]]
)
