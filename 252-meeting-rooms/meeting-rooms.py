class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda pair:pair[0]) #[[2,4], [7,10]]

        for i in range(1, len(intervals)):
            i2 = intervals[i] #1
            i1 = intervals[i-1] #0

            if i1[1] <= i2[0]:
                continue
            return False
        return True
