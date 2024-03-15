class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
#         split_s = s.split(' ')
#         result = []
#         for i in split_s:
#             if i == '':
#                 continue
#             result.append(i)
#         return ' '.join(result[::-1])
        
        result = ''
        
        temp = ''
        for i in s:
            if i == ' ':
                if temp != '':
                    result = ' '+temp+result
                temp = ''
            else:
                temp += i
        if temp != '':
            result = ' '+temp+result
        
        return result[1:]