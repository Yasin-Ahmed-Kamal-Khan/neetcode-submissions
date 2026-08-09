class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while True:
                if len(stack) == 0:
                    stack.append((temp, i))
                    break

                last = stack[len(stack) - 1]
                if temp > last[0]:
                    res[last[1]] = i - last[1]
                    stack.pop()
                else:
                    stack.append((temp, i))
                    break
        return res

        