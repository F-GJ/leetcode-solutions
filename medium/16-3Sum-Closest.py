"""
Question Link : https://leetcode.com/problems/3sum-closest/description/?envType=problem-list-v2&envId=array&

You are given an integer array nums of length n and an integer target.
Find three integers at distinct indices in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == target:
                    return current_sum

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                else:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
        return closest_sum


print("=" * 30)
print("<>" * 15)
print("=" * 30, "\n")
print("Example 1")
example_1 = Solution()
print("Input: nums = [-1,2,1,-4], target = 1")
print(f"Output: {example_1.threeSumClosest([-1, 2, 1, -4], 1)} \n")

print("=" * 30)
print("<>" * 15)
print("=" * 30, "\n")
print("Example 2")
example_2 = Solution()
print("Input: nums = [0,0,0], target = 1")
print(f"Output: {example_2.threeSumClosest([0, 0, 0], 1)} \n")
