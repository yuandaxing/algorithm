def GCD (x, y):
    while y != 0 :
        x, y = y, x % y
    return x
def Normalize(x, y) :
    if x * y == 0 :
        return 1 if x else 0, 1 if y else 0
    else :
        sign = 1 if x * y > 0 else -1
        x, y = abs(x), abs(y)
        c = GCD(x, y)
        return x / c, sign * y / c
class Solution :
    def maxPoints(self, points):
        maxNum = 0
        result = []
        for index, point in enumerate(points) :
            K = {(0,0):[index]}
            for idx in range(index+1, len(points)):
                p = points[idx]
                gradient = Normalize(p.x - point.x, p.y - point.y)
                K.setdefault(gradient, [])
                K[gradient].append(idx)
            for key in K :
                curLen = len(K[key])  
                if key != (0, 0) :
                    curLen += len(K[(0,0)])
                maxNum = maxNum if maxNum > curLen else curLen
        return maxNum
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

testCase = [
    [Point(1,2), Point(2,3), Point(3,4), Point(4,6), Point(8, 12)]
    ]

sol = Solution();
for test in testCase :
    print sol.maxPoints(test)

            
