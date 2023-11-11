class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {"I":1,"IV":4,"V":5,"IX":9,"X":10,"XL":40,"L":50,"XC":90,"C":100,"CD":400,"D":500,"CM":900,"M":1000}
        strlen = len(s)
        i=0
        num = 0
        while i<strlen:
            if i+1<strlen and s[i:i+2] in roman_map:
                num+=roman_map[s[i:i+2]]
                i+=2
            else:
                num+=roman_map[s[i]]
                i+=1
        return num
