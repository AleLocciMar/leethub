class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) == 0 or len(s) == 1:
            return False
        for c in s:
            if c == "(" or c == "[" or c == "{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if stack[-1] == "(" and c == ")":
                        stack.pop()
                    elif stack[-1] == "[" and c == "]":
                        stack.pop()
                    elif stack[-1] == "{" and c == "}":
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        return False
        