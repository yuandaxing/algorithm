class Solution:
	# @param s, a string
	# @return a list of lists of 
	def partition(self, s):
	        def isPal(i, j) :
		        while i < j and s[i] == s[j] :
			        i, j = i+1, j-1
			return i >= j
		def auxRecus(j) :
		        if j >= len(s) :
			        return [[]]
			res = []
			for k in range(j, len(s)) :
			        if isPal(j, k):
				        cur = auxRecus(k+1)
				        map(lambda x : x.append(s[j:k+1]), cur)
				        res.extend(cur)
			return res
		result = auxRecus(0)
		map(lambda x : x.reverse(), result)
		return result


test = 'aab'
sol = Solution()
print sol.partition(test)
		
