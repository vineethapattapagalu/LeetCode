class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        sum_money = [sum(i) for i in accounts]
        return max(sum_money)