class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 3:
            if sum(nums) == 0:
                return [nums]
            else:
                return []
        nums.sort()
        print(nums)
        result = set()
        for i in range(len(nums)-2):
            l = i+1
            h = len(nums)-1
            while l<h:
                if nums[l]+nums[h]+nums[i]==0:
                    result.add(tuple([nums[i], nums[l], nums[h]]))
                    l += 1
                    h -= 1
                elif nums[l]+nums[h]+nums[i]<0:
                    l += 1
                else:
                    h -= 1
        return list(result)
                
            
        