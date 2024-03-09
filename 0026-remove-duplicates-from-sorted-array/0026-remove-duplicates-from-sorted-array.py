class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        i , j =0, 1
        while j < len(nums):
            if nums[j] != nums[j-1]:
                nums[i+1] = nums[j]
                i += 1
            j += 1
        return i+1
        