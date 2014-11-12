class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if not num : 
            return None

        l, r = 0, len(num)-1
        while l < r and num[l] > num[r] :
            mid = (l + r) / 2
            if num[mid] > num[l] :
                l = mid + 1
            else :
                r = mid 
        return num[l]

A = [4,5, 6, 7, 0, 1, 2]
s = Solution()
print s.findMin(A)
