class Solution:
    # @param tokens, a list of string
    # @return an integer
    def evalRPN(self, tokens):
        stack = []
        for token in tokens :
            if token not in ['+', '-', '*', '/']:
                stack.append(int(token))
            else :
                b = stack.pop()
                a = stack.pop()
                if token == '+' :
                    stack.append(a+b)
                elif token == '-' :
                    stack.append(a-b)
                elif token == '/' :
                    sign = 1 if a * b > 0 else -1;
                    result = (abs(a)/abs(b)) * sign
                    stack.append(result)
                else :
                    stack.append(a*b)
        return stack.pop()

testcase = [["2", "1", "+", "3", "*"],
            ["4", "13", "5", "/", "+"],
            ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
            ]

sol = Solution()
for test in testcase :
    print sol.evalRPN(test)
