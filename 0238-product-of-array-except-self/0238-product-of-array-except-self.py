class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left_accum = [1]
        right_accum = [1]
        temp = 1
        for i in nums:
            temp = temp*i
            left_accum.append(temp)
        nums = nums[::-1]
        temp = 1
        for i in nums:
            temp = temp*i
            right_accum.append(temp) 
        right_accum = right_accum[::-1]
        result= []
        print(left_accum, right_accum)
        for i in range(len(left_accum)-1):
            result.append(left_accum[i]*right_accum[i+1])
        return result
            
        
            
            