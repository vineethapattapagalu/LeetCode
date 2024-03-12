class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        pattern_list = list(pattern)
        s_list = s.split(' ')
        if len(pattern_list) != len(s_list):
            return False
        dic = {}
        dic1 = {}
        
        for i in range(len(pattern_list)):
            if pattern_list[i] not in dic and s_list[i] not in dic1:
                dic[pattern_list[i]] = s_list[i]
                dic1[s_list[i]] = pattern_list[i]
            elif (pattern_list[i]  in dic and s_list[i] not in dic1) or (pattern_list[i] not in dic and s_list[i]  in dic1):
                return False
            else:
                if (dic[pattern_list[i]] != s_list[i]) or (dic1[s_list[i]] != pattern_list[i]):
                    return False
        return True
        