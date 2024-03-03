class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack_open = []
        dict_open = {')' : '(', '}':'{', ']':'['}
        
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack_open.append(i)
            else:
                if stack_open:
                    element = stack_open.pop(-1)
                    if element != dict_open[i]:
                        return False
                else:
                    return False
        if len(stack_open):
            return False
        return True