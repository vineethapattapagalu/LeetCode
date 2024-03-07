class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if len(str(num))  == 1:
            return num
        
        while len(str(num)) > 1:
            num = sum(list(map(int, str(num))))
        return num