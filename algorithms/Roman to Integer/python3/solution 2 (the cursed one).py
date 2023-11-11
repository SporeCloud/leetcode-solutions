class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        s = s.replace("IV","IIII").replace("IX","IIIIIIIII").replace("XL","XXXX").replace("XC","XXXXXXXXX").replace("CD","CCCC").replace("CM","CCCCCCCCC")
        num = 0
        for char in s:
            num+=roman_map[char]
        return num
