class Solution:
    def countDays(self, days, meetings):
        meetings = sorted(meetings, key=lambda x: x[0])
        temp = []
        for i in meetings:
            if not temp or temp[-1][1] < i[0]:
                temp.append(i)
            else:
                temp[-1][1] = max(temp[-1][1], i[1])

        res = 0

        for i in range(1, len(temp)):
            if temp[i][0] <= days:
                res += min(temp[i][0], days) - temp[i - 1][1] - 1

        if temp[0][0] > 1:
            res += temp[0][0] - 1

        if temp[-1][1] < days:
            res += days - temp[-1][1]

        return res
