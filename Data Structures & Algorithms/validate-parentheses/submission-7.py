class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for char in s:
            if char in {'{', '(', '['}:
                stack.append(char)
            elif len(stack) == 0:
                return False
            elif char == '}':
                if stack.pop() != '{':
                    return False
            elif char == ']':
                if stack.pop() != '[':
                    return False
            elif stack.pop() != '(':
                return False

        return len(stack) == 0