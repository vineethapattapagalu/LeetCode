class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        dic = {}
        for i in range(65, 91):
            dic[chr(i)] = i-64
        result = 0
        for i in range(len(columnTitle)):
            result = result*26 + dic[columnTitle[i]]
        return result