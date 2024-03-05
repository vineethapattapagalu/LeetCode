class Solution(object):
    def minimumLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        list_s = list(s)
        l = 0
        h = len(list_s)-1
        while l<=h:
            left_char = list_s[l]
            right_char = list_s[h]
            if l == h or left_char != right_char:
                return h+1-l
            while True:
                l += 1
                if l>=len(list_s) or left_char != list_s[l]:
                    break
            while True:
                h -= 1
                if h<0 or right_char != list_s[h]:
                    break
        return 0
        