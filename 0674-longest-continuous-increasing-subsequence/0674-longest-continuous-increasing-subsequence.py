class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 1
        temp_result = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                temp_result += 1
            else:
                temp_result = 1
            result = max(result, temp_result)
        return result
                
        