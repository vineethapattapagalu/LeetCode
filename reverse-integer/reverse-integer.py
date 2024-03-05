class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = (-1)*x
        result = 0
        while x:
            result = result*10 + x%10
            x = x//10
        if result < pow(-2, 31)-1 or result > pow(2, 31):
            return 0
        return sign*result