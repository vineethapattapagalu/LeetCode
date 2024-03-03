class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        ransomeNote_dict = {}
        magazine_dict = {}
        
        for i in magazine:
            if i not in magazine_dict:
                magazine_dict[i] = 1
            else:
                magazine_dict[i] += 1
        for i in ransomNote:
            if i not in ransomeNote_dict:
                ransomeNote_dict[i] = 1
            else:
                ransomeNote_dict[i] += 1
        for key, value in ransomeNote_dict.items():
            if key in magazine_dict and value <= magazine_dict[key]:
                continue
            else:
                return False
        return True
        