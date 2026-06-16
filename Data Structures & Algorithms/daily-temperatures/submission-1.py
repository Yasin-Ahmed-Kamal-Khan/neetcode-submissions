from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        results: List[int] = [0 for i in temperatures]

        if len(temperatures) == 0:
            return []

        stack = []
        stack.append((0, temperatures[0]))

        for current_index, current_temp in enumerate(temperatures):
            while stack:
                top_index, top_temp = stack[-1]
                if top_temp >= current_temp:
                    break

                results[top_index] = current_index - top_index
                stack.pop()

            stack.append((current_index, current_temp))

        return results
