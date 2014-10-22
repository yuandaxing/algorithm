class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        if not num : return None
        left, right = 0, len(num)-1
        while left + 1 < right :
            mid = (left+right)/2
            if num[mid] > num[left] :
                if num[left] >= num[right] :
                    left = mid
                else :
                    right = mid
            elif num[mid] == num[left] :
                left += 1
            elif num[mid] < num[right] :
                right = mid 
            else :
                right -= 1
        return  min(num[left], num[right])

A = [4, 5, 6, 7, 0, 1, 2]
s = Solution()
print s.findMin(A)
