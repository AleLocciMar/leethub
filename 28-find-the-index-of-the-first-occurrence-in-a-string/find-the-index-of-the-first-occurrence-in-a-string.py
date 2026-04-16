class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack.__contains__(needle):
            return -1
        return haystack.find(needle)
        
        