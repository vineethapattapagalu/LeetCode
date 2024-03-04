class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l = 0
        h = len(nums)-1
        mid = (l+h)//2
        while l<=h:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                h = mid-1
            mid = (l+h)//2
        return -1
        