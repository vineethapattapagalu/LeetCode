class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 0
        result = 0
        while True:
            i += 1
            if n-i >=0 :
                result += 1
                n -= i
            else:
                break
        return result
        