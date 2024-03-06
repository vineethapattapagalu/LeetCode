class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carrier = 0
        i , j = len(a)-1 , len(b)-1
        result = ''
        while i >= 0 and j >= 0:
            sum_Val = int(a[i])+int(b[j])+carrier
            result = str(sum_Val%2)+result
            carrier = sum_Val//2
            i -= 1
            j -= 1
        while i>=0:
            sum_Val = int(a[i])+carrier
            result = str(sum_Val%2)+result
            carrier = sum_Val//2
            i -= 1
        while j>=0:
            sum_Val = int(b[j])+carrier
            result = str(sum_Val%2)+result
            carrier = sum_Val//2
            j -= 1
        if carrier:
            result = str(carrier)+result
        return result
                
                
            
            
            