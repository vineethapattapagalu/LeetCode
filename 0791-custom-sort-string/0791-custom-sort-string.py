class Solution(object):
    def customSortString(self, order, s):
        """
        :type order: str
        :type s: str
        :rtype: str
        """
        
        result = ''
        temp_result = ''
        for i in order:
            if i in s:
                count_char = s.count(i)
                result += i*count_char
            
        for j in s:
            if j not in order:
                temp_result += j
        return result+temp_result