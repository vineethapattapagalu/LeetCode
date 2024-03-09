class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = ''
        rev_result = ''
        print(ord('0'))
        for i in s:
            if ord(i) >= 65 and ord(i) < 91:
                result += chr(ord(i)+32)
                rev_result = chr(ord(i)+32) + rev_result
            elif (ord(i) >= 97 and ord(i) < 123) or (ord(i) >= 48 and ord(i) < 58):
                result += chr(ord(i))
                rev_result = chr(ord(i)) + rev_result
                
        if result == rev_result:
            return True
        return False