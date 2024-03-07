class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic1 = {}
        for i in range(len(nums)):
            if nums[i] not in dic1:
                dic1[nums[i]]  = i
            elif i-dic1[nums[i]] <= k:
                return True
            else:
                dic1[nums[i]] = i
        return False
        
        