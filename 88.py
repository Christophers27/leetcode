class Solution:
    def merge(self, nums1, m, nums2, n):
        point1, point2, point = m - 1, n - 1, m + n - 1

        while point1 >= 0 and point2 >= 0:
            if nums1[point1] > nums2[point2]:
                nums1[point] = nums1[point1]
                point1 -= 1
            else:
                nums1[point] = nums2[point2]
                point2 -= 1

            point -= 1

        while point2 >= 0:
            nums1[point] = nums2[point2]
            point -= 1
            point2 -= 1
