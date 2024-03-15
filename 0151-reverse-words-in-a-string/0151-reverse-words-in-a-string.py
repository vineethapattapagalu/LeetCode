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
        
        s_list = []
        
        temp = ''
        for i in s:
            if i == ' ':
                if temp != '':
                    s_list.append(temp)
                temp = ''
            else:
                temp += i
        if temp != '':
            s_list.append(temp)
        print(s_list)
        s_list = s_list[::-1]
        return ' '.join(s_list)