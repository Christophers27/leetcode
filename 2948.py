class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        N = len(nums)
        withIndex = [(nums[i], i) for i in range(N)]
        withIndex.sort(key=lambda x: x[0])

        grouped = [[withIndex[0]]]
        for i in range(1, N):
            if withIndex[i][0] - withIndex[i - 1][0] <= limit:
                grouped[-1].append(withIndex[i])
            else:
                grouped.append([withIndex[i]])

        # Sort within each group
        for group in grouped:
            indices = [x[1] for x in group]
            indices.sort()

            for i in range(len(group)):
                nums[indices[i]] = group[i][0]

        return nums
