# 2024-09-23
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:

        minutes = []

        for time in timePoints:
            hr, mi = map(int, time.split(":"))
            minute = hr * 60 + mi
            if minute in minutes:
                return 0
            minutes.append(minute)

        minutes.sort()

        min_diff = float('inf')
        for i in range(1, len(minutes)):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])

        return min(min_diff, 24*60 - minutes[-1] + minutes[0])