class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == " ":
            return len(s)
        elif len(s) == 1:
            return 1
       
        char_set = set()
        esquerda = 0
        maior_comprimento = 0

        for direita in range(len(s)):
            while s[direita] in char_set:
                char_set.remove(s[esquerda])
                esquerda += 1

            char_set.add(s[direita])
            
            maior_comprimento = max(maior_comprimento, direita - esquerda + 1)

        return maior_comprimento


        