class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        split_s = s.split(' ')
        result = []
        for i in split_s:
            if i == '':
                continue
            result.append(i)
        print(result)
        return ' '.join(result[::-1])
        