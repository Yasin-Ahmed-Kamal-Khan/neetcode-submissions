class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    stack: list[int] = []

    for i in tokens:
        if i not in ('+', '-', '/', '*'):
            stack.append(int(i))
            continue

        second = stack.pop()
        first = stack.pop()
        
        if i == '+':
            stack.append(first + second)
        elif i == '-':
            stack.append(first - second)
        elif i == '*':
            stack.append(first * second)
        elif i == '/':
            stack.append(int(first / second))

    return stack.pop()

