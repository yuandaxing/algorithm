class Solution:
	# @return a string
	def convert(self, s, nRows):
		res =[[] for i in range(nRows)]
		cycle = 2 * nRows - 2
		if nRows == 1 : return s
		for i in range(0, len(s)) :
			remain = i % cycle
			res[remain if remain < nRows else cycle - remain].append(s[i])
		return reduce(lambda x, y : \
		              x + ''.join(y), res, '')
	def convert1(self, s, nRows) :
		return s
		

test = 'PAYPALISHIRING'
sol = Solution()
print sol.convert(test, 3)
			
