class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        sign = (divisor > 0 and dividend > 0) or \
               (dividend <= 0 and divisor <= 0)
        dividend, divisor = abs(dividend), abs(divisor)
        possibleDiv, count = [], 1
        while dividend >= divisor :
            possibleDiv.append([divisor, count]) 
            divisor, count = divisor + divisor, count + count
        possibleDiv.reverse()
        res = 0
        for elem in possibleDiv :
            if dividend >= elem[0] :
                res, dividend = res + elem[1], dividend - elem[0]
        return res if sign else -res


sol = Solution()
print sol.divide(10, 2)
            
