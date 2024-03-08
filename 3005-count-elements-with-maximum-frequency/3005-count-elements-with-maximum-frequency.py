class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums_dic = {}
        for i in nums:
            if i not in nums_dic:
                nums_dic[i] = 1
            else:
                nums_dic[i] += 1
        max_val = max(nums_dic.values())
        result = [key for key, value in nums_dic.items() if value == max_val]

        return len(result)*max_val