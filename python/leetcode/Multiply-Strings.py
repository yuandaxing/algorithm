class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply_num(self, arr, num) :
        result, c = [], 0
        for a in arr :
            cur = num * a + c
            result.append(cur % 10)
            c = cur / 10
        if c :
            result.append(c)
        return result
    
    def add_array(self, arr1, arr2) :
        result, c = [], 0
        for i in range(max(len(arr1), len(arr2))) :
            a = 0 if i >= len(arr1) else arr1[i]
            b = 0 if i >= len(arr2) else arr2[i]
            v = a + b + c
            c = v / 10
            result.append(v % 10)
        if c :
            result.append(c)
        return result

    def shitf_k(self, arr1, k) :
        result = list(arr1) 
        zero = [0 for i in range(k)]
        result = zero + result
        return result
        
    def multiply(self, num1, num2):
        result = []
        arr1 = [int(num1[len(num1)-1-i]) for i in range(len(num1))]
        arr2 = [int(num2[len(num2)-1-i]) for i in range(len(num2))]
        for i in range(len(arr2)) :
            cur = self.multiply_num(arr1, arr2[i])
            cur = self.shitf_k(cur, i)
            result = self.add_array(result, cur)
        
        result = result[-1::-1]
        while result :
            if not result[0]:
                result.pop(0)
            else :
                break
        if not result : result.append(0)
        return ''.join(map(lambda e : str(e), result))
            


s1 = "123"
s2 = "12"

sol = Solution()
print sol.multiply(s1, s2)
print sol.multiply('9', '9')
print sol.multiply('99999999', '0')
