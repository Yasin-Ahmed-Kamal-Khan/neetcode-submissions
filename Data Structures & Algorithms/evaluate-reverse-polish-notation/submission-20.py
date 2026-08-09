class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {'+', '-', '*', '/'}:
                stack.append(int(t))
            else:
                # print(stack)
                num2 = stack.pop()
                num1 = stack.pop()
                res = None
                if t == '+':
                    res = num1 + num2 
                elif t == '-':
                    res = num1 - num2
                elif t == '*':
                    res = num1 * num2
                else: 
                    res = int(num1 / num2)
                # print(res)
                stack.append(res)

        return stack.pop()

