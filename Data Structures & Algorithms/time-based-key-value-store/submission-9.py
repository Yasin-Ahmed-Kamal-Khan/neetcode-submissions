class TimeMap:

    def __init__(self):
        self.timeMap = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if self.timeMap.get(key) is None:
            self.timeMap[key] = ([timestamp], {timestamp: value})
            return

        timestamps, timeVal = self.timeMap[key]

        timestamps.append(timestamp)
        timeVal[timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if self.timeMap.get(key) is None:
            return ""

        timestamps, timeVal = self.timeMap[key]

        left, right = 0, len(timestamps) - 1

        biggest = left
        while left <= right:
            middle = (left + right) // 2
            if timestamps[middle] <= timestamp:
                biggest = middle
                left = middle + 1
            else:
                right = middle - 1

        if timestamps[biggest] > timestamp:
            return ""
        
        return timeVal[timestamps[biggest]]

