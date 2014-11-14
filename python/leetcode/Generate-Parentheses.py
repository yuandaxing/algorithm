class Solution:
    # @param an integer
    # @return a list of string
    # P(N) = P(1) * P(N-1) + P(N-1) * P(1) + P(2) * P(N-2) +
    # P(N-2) * P(2) + 1
    def generateParenthesis(self, n):
        if n == 0 :
            return ''
        if n == 1 :
            return '()'
        for i in range(n) :
            left = self.generateParenthesis(i)
