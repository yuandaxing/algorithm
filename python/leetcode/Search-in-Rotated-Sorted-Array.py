class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    def search(self, A, target):
        left, right = 0, len(A)-1
        while left + 1 < right :
            mid = (left+right)/2
            if A[mid] >= A[left] :
                if A[mid] >= target and A[left] <= target :
                    right = mid 
                else :
                    left = mid 
            else :
                if A[mid] <= target and A[right]>= target :
                    left = mid
                else :
                    right = mid
        return left if A[left] == target else \
            (right if A[right] == target else -1)


    def search1(self, A, target):
        left, right = 0, len(A)-1
        while left <= right :
            mid = (left+right)/2
            if A[mid] == target :
                return mid
            elif A[mid] >= A[left] :
                if A[mid] > target and A[left] <= target :
                    right = mid -1
                else :
                    left = mid + 1
            else :
                if A[mid] < target and A[right]>= target :
                    left = mid + 1
                else :
                    right = mid - 1
        return -1



A = [4, 5, 6, 7, 0, 1, 2]
s = Solution()
print s.search(A, 6)
