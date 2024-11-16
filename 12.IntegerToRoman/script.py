class Solution(object):
    def intToRoman(self, num):
        numbers = [int(x) for x in str(num)]  
    
        values = {
                1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
                10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
            
        result = ""
            
        for value, symbol in sorted(values.items(), reverse=True):
            while num >= value:
                result += symbol
                num -= value
            
        return result


        
        