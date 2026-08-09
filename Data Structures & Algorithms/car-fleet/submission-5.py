class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = zip(position, speed)
        pairs = sorted(pairs, key = lambda x: x[0], reverse = True)
        
        stack = []
        for pos, s in pairs:
            arrivalTime = (target - pos) / s
            if len(stack) == 0:
                stack.append(arrivalTime)
            elif stack[len(stack) - 1] < arrivalTime:
                stack.append(arrivalTime)

        return len(stack)