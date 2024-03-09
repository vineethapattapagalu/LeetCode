class Solution(object):
    def getCommon(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        min_val = nums1[0]
        i, j = 0, 0
        
        while i < len(nums1):
            element = nums1[i]
            while j < len(nums2):
                if nums2[j] < nums1[i]:
                    j += 1
                elif nums2[j] == nums1[i]:
                    return nums1[i]
                else:
                    break
            i += 1
        return -1
            