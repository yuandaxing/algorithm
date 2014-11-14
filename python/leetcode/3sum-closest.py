class Solution:
    # @return an integer
    def twoCloset(self, num, i, target ) :
        left, right = i, len(num) -1 
        MIN = num[left]+num[right] - target
        while left < right :
            diff = num[left] + num[right] - target 
            if abs(MIN) > abs(diff) :
                MIN = diff
            if diff > 0 :
                right -= 1
            else :
                left += 1
        return MIN
    def threeSumClosest(self, num, target):
        num.sort()
        for i in range(len(num)) :
            for j in range(i+1, len(num)-2) :
                  
        
