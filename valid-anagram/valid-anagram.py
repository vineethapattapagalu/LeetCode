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
                
        for j in t:
            if j not in dic:
                return False
            else:
                dic[j] -= 1
        for key, value in dic.items():
            if value != 0:
                return False
        return True