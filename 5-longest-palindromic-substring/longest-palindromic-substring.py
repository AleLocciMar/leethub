class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s: return ""
        
        res = ""
        for i in range(len(s)):
            # Caso 1: Palíndromo Ímpar (ex: "aba", centro é 'b')
            tmp = self.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp
            
            # Caso 2: Palíndromo Par (ex: "abba", centro é o espaço entre 'b' e 'b')
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    def helper(self, s, l, r):
        # Expande para os lados enquanto as letras forem iguais
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        # Retorna a fatia que é palíndromo
        return s[l+1:r]