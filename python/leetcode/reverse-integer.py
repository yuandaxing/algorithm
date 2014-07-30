class Solution:
	# @return an integer
	def reverse(self, x):
		sign = -1 if x < 0 else 1
		x *= sign
		res = 0
		while x != 0 :
			rem = x % 10
			x /= 10
			res = res * 10 + rem
		return res * sign

sol = Solution()
print sol.reverse(123)
print sol.reverse(-123)
