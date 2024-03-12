class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result_5 = 0
        
        for i in range(1, n+1):
            
            while True:
                if i%5 != 0:
                    break
                i = i//5
                result_5 += 1
            
        return result_5
                
                
            