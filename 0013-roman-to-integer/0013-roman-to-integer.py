class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_to_int = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D': 500, 'M': 1000}
        prev_char = ''
        curr_char = ' '
        result = 0
        for i in s:
            curr_char = i
            if prev_char:
                if roman_to_int[prev_char] < roman_to_int[curr_char]:
                    result += roman_to_int[curr_char]
                    result -= 2*roman_to_int[prev_char]
                else:
                    result += roman_to_int[curr_char]
            else:
                result += roman_to_int[curr_char]
            prev_char = curr_char
        return result
            
        