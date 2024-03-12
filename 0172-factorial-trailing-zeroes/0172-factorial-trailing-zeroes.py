class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result_5 = 0
        result_2 = 0
        
        for i in range(1, n+1):
            
            while True:
                if i%5 != 0:
                    break
                i = i//5
                result_5 += 1
            while True:
                if i%2 != 0:
                    break
                i = i//2
                result_2 += 1
        return min(result_2, result_5)
                
                
            