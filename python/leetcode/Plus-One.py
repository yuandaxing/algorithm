class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry, i, res = 1, 0, []
        for j in range(len(digits)) :
            i = len(digits) - 1 - j
            z = digits[i] + carry
            digits[i], carry = z % 10, z / 10
            if carry == 0 : break
        if carry != 0 :
            digits.insert(0, 1)
        return digits


sol = Solution()
print sol.plusOne([9])
