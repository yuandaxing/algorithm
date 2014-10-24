class Solution:
    # @param a, a string
    # @param b, a string
    # @return a string
    def addBinary(self, a, b):
        a = map(lambda x : int(x), a)
        b = map(lambda x : int(x), b)
        a, b, c = a[-1::-1], b[-1::-1], 0
        result = []
        for i in range(max(len(a), len(b))) :
            ba = 0 if i >= len(a) else a[i]
            bb = 0 if i >= len(b) else b[i]
            z = ba+bb+c
            result.append(z % 2)
            c = z / 2
        if c :
            result.append(c)
        result = map(str, result)[-1::-1]
        return ''.join(result)


a = '11'
b = '1'
sol = Solution()
print sol.addBinary(a, b)
            
