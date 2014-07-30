class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        left, right = 0, len(A)-1
        while left <= right :
            mid = (left + right) / 2
#            print mid
            v = A[mid]
            if v == target :
                return mid
            elif v > target :
                right = mid - 1
            else :
                left = mid + 1
        return left
sol = Solution()
print sol.searchInsert([1], 1)
