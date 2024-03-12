class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        if x < 0:
            return False
        result = 0
        temp_x = x
        while x:
            result = result*10 + x%10
            x = x//10
        return result == temp_x
        