class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in index_dict:
                return [i, index_dict[target-nums[i]]]
            index_dict[nums[i]] = i
            
        