class Solution:
	# @return a float
	# A[0....N], B[0....M] mid = (N+M+2)/2
	#  if A[j] is the mid then A[j-1] <= A[j] <= A[j+1] and 
	#  A[j] >= B[mid-j] && A[j-1] <= B[mid-j+1]
	def findMedianSortedArrays(self, A, B):
		def auxfind(arr1, arr2) :
			len1, len2 = len(arr1), len(arr2)
			mid = (len1 + len2) / 2
			i, j = 0, len1 - 1
			while i <= j :
				m = (i + j) / 2
				k = mid - m - 1
				#print i, j, m, k 
				if k + 1 < 0 :
					j = m - 1
				elif k >= len2 :
					i = m + 1
				elif k >= 0 and k < len2 and \
				     arr1[m] < arr2[k] :
					i = m + 1
				elif k + 1 >= 0 and k + 1 < len2 and \
				     arr1[m] > arr2[k+1] :
					j = m - 1 
				else :
					return m
			
			return None
		res1 = auxfind(A, B)
		if res1 != None :
			return A[res1]
		else :
			res2 = auxfind(B, A)
			return B[res2]

#Array1 = [1, 3, 5, 7, 9]
#Array2 = [2, 4, 6]
Array1 = []
Array2 = [1]
Sol = Solution()
print Sol.findMedianSortedArrays(Array1, Array2)
