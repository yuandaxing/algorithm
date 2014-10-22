class Solution:
    # @param root, a tree node
    # @return a boolean
    # isBalancedAux return (isb, height) 
    # left,right = isBalancedAux(root.left), isBalancedAux(root.right) 
    # if left[0] and right[0] and abs(left[1]-right[1]) <= 1 :
    #     return (True, max(left[1], right[1])+1)
    # return (False, 0)
    def isBalancedAux(self, root) :
        if not root :
            return (True, 0)
        else :
            left, right = self.isBalancedAux(root.left), \
                          self.isBalancedAux(root.right)
            if left[0] and right[0] and abs(left[1]-right[1]) <= 1 :
                return (True, max(left[1], right[1])+1)
            else :
                return (False, 0)
    def isBalanced(self, root):
        return self.isBalancedAux(root)[0]

class Tree :
    def __init__(self, left, right, val) :
        self.left = left
        self.right = right
        self.val = val

t1, t2 = Tree(None, None, 0), Tree(None, None, 0)
t3 = Tree(t1, t2, 0)
sol = Solution()
print sol.isBalanced(t3)


