class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic = {} 
        dic1 = {}
        
        for i in range(len(s)):
            if s[i] not in dic and t[i] not in dic1:
                dic[s[i]] = t[i]
                dic1[t[i]] = s[i]
                
            elif (s[i] not in dic and t[i] in dic1) or (s[i]  in dic and t[i] not in dic1):
                return False
            elif s[i] in dic and t[i] in dic1:
                if dic[s[i]] == t[i] and dic1[t[i]] == s[i]:
                    continue
                else:
                    return False
        return True
                
                
            