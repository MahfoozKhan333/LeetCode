class Solution:
    def maxProduct(self, n):
        digits = [int(d) for d in str(n)]
        maxProd = 0
        for i in range(len(digits)):
            for j in range(i, len(digits)):
                if i !=j:
                    maxProd = max(maxProd, digits[i] * digits[j])
        return maxProd
