class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        copy = nums1[:m]
        i1, i2 = 0, 0
        while i1 < m and i2 < n:
            if copy[i1] <= nums2[i2]:
                nums1[i1 + i2] = copy[i1]
                i1 += 1
            else:
                nums1[i1 + i2] = nums2[i2]
                i2 += 1

        if i1 == m:
            nums1[(i1 + i2):] = nums2[i2:]

        if i2 == n:
            nums1[(i1 + i2):] = copy[i1:]
