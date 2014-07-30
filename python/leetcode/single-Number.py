class Solution:
	# @param A, a list of integer
	# @return an integer
	def singleNumber(self, A):
		return reduce(lambda x, y : x ^ y, A, 0)

sol = Solution()
print sol.singleNumber([1, 1, 2, 3, 3, 4, 4])
