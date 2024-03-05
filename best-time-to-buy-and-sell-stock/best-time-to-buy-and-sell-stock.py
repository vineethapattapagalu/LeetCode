class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        min_val = prices[0]
        for i in range(1, len(prices)):
            result = max(result, prices[i]-min_val)
            min_val = min(min_val, prices[i])
        return result
                
        