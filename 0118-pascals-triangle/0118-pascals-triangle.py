class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = [[1]]
        for i in range(1, numRows):
            temp_list = [result[-1][0]]
            for j in range(len(result[-1])-1):
                temp_list.append(result[-1][j] + result[-1][j+1])
            temp_list.append(result[-1][-1])
            result.append(temp_list)
        return result
            
        