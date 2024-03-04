class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        len_s = len(s)
        no_of_1 = 0
        for i in s:
            if i == '1':
                no_of_1 += 1
        result = ''
        while len_s > 1:
            if no_of_1 > 1 and len_s > 1:
                result += '1'
                no_of_1 -= 1
                len_s -= 1
            if no_of_1 == 1 and len_s > 1:
                result += '0'
                len_s -= 1
        return result+'1'
                
            
            
        