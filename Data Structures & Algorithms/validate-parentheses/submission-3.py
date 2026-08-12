class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        char_map = {"(":")",
                "[":"]",
                "{":"}"}
        for char in s:
            if char in ["(","[","{"]:
                stack.append(char)
            elif stack and char == char_map[stack[-1]]:
                stack.pop()
            else:
                return False
        if not stack:
            return True
        return False
                
            