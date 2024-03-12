class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        carrier = 1
        temp_digits = digits[::-1]
        for i in range(len(digits)):
            val = (temp_digits[i]+carrier)
            temp_digits[i] = val%10
            carrier = val//10
            print(temp_digits)
        temp_digits = temp_digits[::-1]
        if carrier:
            temp_digits.insert(0, 1)
        return temp_digits