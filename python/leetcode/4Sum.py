class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]
    def find2Sum(self, array, i, j, target) :
        result = []
        while i < j :
            val = array[i] + array[j]
            if val == target :
	        result.append([array[i], array[j]])
                i, j = i+1, j-1
            elif val < target :
		i+=1
            else :
		j-=1
        return result
    def fourSum1(self, num, target):
        num.sort()
        result = []
        for i in range(len(num)) :
            if i > 0 and num[i] == num[i-1] : continue 
            for j in range(i+1, len(num)) :
                a1, a2 = num[i], num[j]
                for s in self.find2Sum(num, j+1, len(num)-1, target - a1 - a2) :
                    s.append(a1)
                    s.append(a2)
                    s.sort()
                    result.append(s)
        result = set(map(tuple, result))
        result = map(list, result)
        return result 
    def fourSum(self, num, target) :
        num.sort()
        s = {}
        for i in range(len(num)) :
            for j in range(i+1, len(num)) :
                v = num[i] + num[j]
                s.setdefault(v, [])
                s[v].append([num[i], num[j]])
        for i in range(len(num)) :
            if i > 0 and num[i] == num[i-1] : continue 
            for j in range(i+1, len(num)) :
                cur = num[i] + num[j]
                left = target - cur
                if s.containskey(left) :
                    for 


s = [1, 0, -1, 0, -2, 2]
sol = Solution()
print sol.fourSum(s, 0)

        
