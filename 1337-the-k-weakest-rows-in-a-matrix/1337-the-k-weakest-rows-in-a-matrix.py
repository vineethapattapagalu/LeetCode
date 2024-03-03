class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        sum_result = [sum(i) for i in mat]
        dict_sum = {}
        for index, value in enumerate(sum_result):
            dict_sum[index] = value
        result = sorted(dict_sum.items(), key= lambda x:x[1])
        return [i[0] for i in result[:k]]
                
        
        
        