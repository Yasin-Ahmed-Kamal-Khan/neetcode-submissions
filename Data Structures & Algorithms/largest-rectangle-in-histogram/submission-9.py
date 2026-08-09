class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        startEndHeights = []
        for i, h in enumerate(heights):
            if len(stack) == 0:
                stack.append([i, None, h])
            elif h < stack[-1][2]:
                start = i
                while h < stack[-1][2]:
                    last = stack.pop()
                    last[1] = i - 1
                    start = min(last[0], start)
                    startEndHeights.append(last)
                    if len(stack) == 0:
                        break

                stack.append([start, None, h])
            elif h == stack[-1][2]:
                pass
            elif h > stack[-1][2]:
                stack.append([i, None, h])
                
        for triple in stack:
            startEndHeights.append(triple)
        res = 0
        for start, end, height in startEndHeights:
            if end is None:
                end = len(heights) - 1
            area = (end - start + 1) * height 
            res = max(area, res)
        print(startEndHeights)
        return res
