class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        result = 0
        for i in range(0, len(haystack)-len(needle)+1):
            j = 0
            while j < len(needle):
                if needle[j] == haystack[i+j]:
                    j += 1
                else:
                    break
            if j == len(needle):
                return i
        return -1