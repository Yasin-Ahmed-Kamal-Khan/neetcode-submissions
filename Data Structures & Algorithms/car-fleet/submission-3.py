class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if position[0] is None:
            return 0

        timesAndPos: List[Tuple[int, int]] = [
            ((target - p) / s, p) for s, p in zip(speed, position)
        ]
        timesAndPos.sort(reverse=True, key=lambda x: x[1])
        stack: List[int] = [timesAndPos[0][0]]

        for time, pos in timesAndPos[1:]:
            topTime = stack[-1]
            if time > topTime:
                stack.append(time)

        return len(stack)