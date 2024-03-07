class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        dic = {}
        for i in range(65, 91):
            dic[i-64] = chr(i)
        result = ''
        while columnNumber>26:
            if columnNumber % 26 == 0:
                result = dic[26]+result
                columnNumber = columnNumber//26 -1
            else:
                result = dic[columnNumber%26]+result
                columnNumber = columnNumber//26
        result = dic[columnNumber]+result
        return result
            
            
            