class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {}
        
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in t:
            if i not in dic:
                return False
            else:
                dic[i] -= 1
                if dic[i] < 0:
                    return False
        return sum(dic.values()) == 0