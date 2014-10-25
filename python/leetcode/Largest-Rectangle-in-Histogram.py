class Solution:
    # @param height, a list of integer
    # @return an integer
    def tryToExpand(self, height, i) :
        j, k = i, i
        while j >= 0 and height[j] >= height[i] :
            j -= 1
        while k < len(height) and height[k] >= height[i] :
            k += 1
        return (k - j - 1) * height[i]
    def largestRectangleArea1(self, height):
        maxA = 0
        for i in range(len(height)) :
            maxA = max(self.tryToExpand(height, i), maxA)
        return maxA
    @staticmethod 
    def comp(e1, e2) :
        return (e1[1]-e2[1]) if (e1[0] == e2[0]) else (e1[0]-e2[0])
    def largestRectangleArea(self, height):
        h_idx = [(height[i], i) for i in range(height)]
        h_idx = h_idx.sort(cmp=self.comp)
        m_i, m_j = -1, len(height)-1
        maxV = 0
        for i in range(len(height)) :
            count = 0
            if height[mm_i > i  :
                m_i = i
            elif m_j > i :
                m_j = i
            
v = [2,1,5,6,2,3]
sol = Solution()
print sol.largestRectangleArea(v)
        
