class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        tokens.sort()
        l = 0
        h = len(tokens)-1
        temp_score = 0
        score = 0
        while l<=h:
            if tokens[l] <= power:
                temp_score += 1
                power -= tokens[l]
                l += 1
                
            elif tokens[l] > power and score > 0:
                temp_score -= 1
                power += tokens[h]
                h -= 1
            else:
                return score
            score = max(score, temp_score)
        return score
                