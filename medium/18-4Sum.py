"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
"""


class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        quads = []

        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = len(nums) - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total == target:
                        quads.append([nums[i], nums[j], nums[left], nums[right]])

                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1

                    elif total > target:
                        right -= 1
        return quads


example_1 = Solution()
print(example_1.fourSum([1, 0, -1, 0, -2, 2], 0))


example_2 = Solution()
print(example_2.fourSum([2, 2, 2, 2, 2], 8))
