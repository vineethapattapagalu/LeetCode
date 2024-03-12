class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        set_nums = set()
        
        while True:
            result = 0
            while n:
                result += (n%10)**2
                n = n//10
            if result in set_nums:
                return False
            if result == 1:
                return True
            n = result
            set_nums.add(result)
            