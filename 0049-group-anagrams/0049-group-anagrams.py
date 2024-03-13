class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dic = {}
        for i in strs:
            temp_i = ','.join(sorted(i))
            if temp_i not in dic:
                dic[temp_i] = [i]
            else:
                dic[temp_i].append(i)
        result = [value for key, value in dic.items()]
        return result