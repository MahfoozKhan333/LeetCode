class Solution:
    def intToNumber(self, num):
        Number = ""
        storeIntRoman = [
            ["M", 1000], 
            ["CM", 900],
            ["D", 500],
            ["CD", 400],
            ["C", 100],
            ["XC", 90],
            ["L", 50],
            ["XL", 40],
            ["X", 10],
            ["IX", 9],
            ["V", 5],
            ["IV", 4],
            ["I", 1]
        ]
        for roman, value in storeIntRoman:
            while num >= value:
                Number += roman
                num -= value
        return Number

    def romanToInt(self, s):
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev = 0
        for char in reversed(s):
            curr = roman_map[char]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total
