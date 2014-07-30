#00 - 0
#01 - 1
#11 - 3
#10 - 2
class Solution:
	# @return a list of integers
	def grayCode(self, n):
		def aux(k, direc) :
			addTail = [0, 1] if direc else [1, 0]
			return [ k * 2 + z for z in addTail]
		init = [0]
		for i in range(0, n) :
			cur = []
			direc = True
			for k in init :
				cur += aux(k, direc)
				direc = not direc
			init = cur
		return init

sol = Solution()
print sol.grayCode(3)
print sol
