class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i , j = 0, 0
        element_found = 0
        while i< len(s):
            
            while j < len(t):
                if t[j] == s[i]:
                    element_found += 1
                    break
                    
                else:
                    j += 1
            i += 1
            j += 1
        return element_found == len(s)
        