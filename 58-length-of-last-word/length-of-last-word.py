class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arrStr= []
        s = s.strip()
        arrStr= s.split(" ")
        size = len(arrStr) - 1
        arrStr[size] = arrStr[size].strip()
        return len(arrStr[size])
        
        