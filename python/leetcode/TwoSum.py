class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
	        def  find2Sum(array) :
		        i, j = 0, len(array) - 1
		        while i < j :
			        val = array[i][0] + array[j][0]
			        if val == target :
				        return array[i][1], array[j][1]
				elif val < target :
					i+=1
				else :
					j-=1
			return -1, -1
		arrayIdx = [[num[i], i] for i in range(len(num))]
		arrayIdx.sort(key = lambda x : x[0])
		idx1, idx2 = find2Sum(arrayIdx)
		if idx1 > idx2 :
			idx1, idx2 = idx2, idx1
		return idx1+1, idx2+1

array = [2, 7, 11, 15]
target = 9
Sol = Solution()
print Sol.twoSum(array, target)
