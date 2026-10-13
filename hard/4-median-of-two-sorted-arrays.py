# https://leetcode.com/problems/median-of-two-sorted-arrays?envType=problem-list-v2&envId=array


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combined = sorted(nums1 + nums2)
        n = len(combined)
        mid = n // 2

        if n % 2 == 0:
            return (combined[mid - 1] + combined[mid]) / 2
        else:
            return float(combined[mid])
