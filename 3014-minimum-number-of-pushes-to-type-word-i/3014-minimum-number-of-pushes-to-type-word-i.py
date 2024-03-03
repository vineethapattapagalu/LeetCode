class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        word_len = len(word)
        result = 0
        i = 1
        while word_len:
            if word_len >=8:
                result += 8*i
            else:
                result += word_len*i
                return result
            i += 1
            word_len -= 8
        return result
            
        