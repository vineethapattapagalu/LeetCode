class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        result = []
        for i in nums:
            result.append(i*i)
        l = 0
        h = len(result)-1
        sorted_result = len(result)*[0]
        i = len(sorted_result)-1
        while l<=h:
            if result[l] < result[h]:
                sorted_result[i] =  result[h]
                h -= 1

            else:
                sorted_result[i] = result[l]
                l += 1
            i -= 1
        return sorted_result


        
                
