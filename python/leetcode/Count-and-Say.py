class Solution:
    # @return a string
    def segTrans(self, curSeg) :
        lenSeg = len(curSeg) 
        if lenSeg == 0 : return ''
        return str(lenSeg)+ curSeg[0]
    def transform(self, numStr) :
        res, cur, next, Len = '', 0, 0, len(numStr)
        while cur < Len :
            while next < Len and numStr[cur] == numStr[next] :
                next += 1
            res += self.segTrans(numStr[cur:next]) 
            cur = next
        return res
    def countAndSayGen(self):
        cur = '1'
        while True :
            yield cur
            cur = self.transform(cur)
    def countAndSay(self, n) :
        gen = self.countAndSayGen()
        cur = ''
        for i in range(n) :
            cur = gen.next()
        return cur

sol = Solution()
print sol.countAndSay(2)
print sol.countAndSay(3)
        
