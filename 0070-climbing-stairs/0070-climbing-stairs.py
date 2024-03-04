class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        ways_list = [1, 2]
        if n <= 2:
            return ways_list[n-1]
        for i in range(2, n):
            ways_list.append(ways_list[i-1]+ways_list[i-2])
        return ways_list[-1]
        