class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums[0] >= target:
            return 0
        if nums[-1] < target:
            return len(nums)
        l = 0
        h = len(nums)-1
        mid = (l+h)//2
        while l<=h:
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[mid+1] > target:
                    return mid+1
                else:
                    l = mid+1
            else:
                if nums[mid-1] < target:
                    return mid
                else:
                    h = mid-1
            mid = (l+h)//2
        
        
        