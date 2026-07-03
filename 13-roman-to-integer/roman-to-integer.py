class Solution:
    def romanToInt(self, s: str) -> int:
        value_set = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        value = i = 0
        while i < len(s):
            if (i+1 < len(s)) and (value_set[s[i+1]] > value_set[s[i]]):
                value += (value_set[s[i+1]] - value_set[s[i]])
                i += 2
            else:
                value += value_set[s[i]]
                i += 1
        return(value)