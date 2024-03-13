class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return n
        l = 1
        h = n
        left_result = 0
        right_result = 0
        while l<=h:
            
            if left_result and right_result and left_result == right_result and l == h:
                return l
            elif left_result <= right_result:
                left_result += l
                l += 1
            else:
                right_result += h
                h -= 1
        return -1
            
        