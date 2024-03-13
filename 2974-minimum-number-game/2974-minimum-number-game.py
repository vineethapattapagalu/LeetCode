class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        while nums:
            min_element_alice = min(nums)
            nums.remove(min_element_alice)
            min_element_bob = min(nums)
            nums.remove(min_element_bob)
            arr.append(min_element_bob)
            arr.append(min_element_alice)
            
        return arr
        