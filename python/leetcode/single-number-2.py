import random 
class Solution:
	# @param A, a list of integer
	# @return an integer
	# choose a pivot, left < pivot, right >= pivot
	# if left is 3*k, the only one can not in the left, then look up right
	# else look up in the left to find the only one
	# if there is only one, just return that one.
	def singleNumber(self, A):
	        def aux(start, end, offset) :
		        if end - start == 1 :
			        return A[start]
			pivot = A[start + offset % (end - start)]
			save, idx = start, start
			while idx < end :
			        if A[idx] < pivot :
				        A[start], A[idx] = A[idx], A[start]
				        start += 1
				idx+=1
			if (start - save ) % 3 == 0 :
				return aux(start, end, offset + 1)
			else :
				return aux(save, start, offset + 1)
		return aux(0, len(A), 0)

sol = Solution()
print sol.singleNumber([1, 1, 2, 1, 3, 4, 4, 4, 3, 3])
print sol.singleNumber([0, 0, 0, 5])
