class Solution:
    # @return a boolean
    def isValid(self, s):
        if len(s) == 0 : return True
        stack, idx = [], 0
        pairDict = {'[' : ']', '{' : '}', '(' : ')'}
        while idx < len(s) :
            if s[idx] in ['[', '{', '('] :
                stack.append(s[idx])
            else :
                if len(stack) == 0 :
                    return False
                char = stack.pop()
                if s[idx] != pairDict[char] :
                    return False
            idx += 1
        return idx >= len(s) and len(stack) == 0


sol = Solution()
print sol.isValid('()[]{}')
                
        
