"""
Question Link :
Given an integer array nums and an integer k,
return true if there are two distinct indices i and j in the array such
that nums[i] == nums[j] and abs(i - j) <= k.

Example 1:
Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:
Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""

nums = [1, 9, 9, 1, 1]
k = 1


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        print(f"Input: nums = {nums}, k = {k}")
        print("Starting dictionary:", seen)
        print()

        for i, num in enumerate(nums):
            print("-------------------------")
            print(f"Current index: {i}")
            print(f"Current number: {num}")
            print(f"Dictionary BEFORE: {seen}")

            if num in seen:
                print(f"We've seen {num} before!")
                print(f"Previous index: {seen[num]}")

                # Step 2: Calculate the distance between the indices
                distance = i - seen[num]

                print(f"Distance: {i} - {seen[num]} = {distance}")
                print(f"Is {distance} <= {k}? {distance <= k}")

                # Step 3: If the duplicate is close enough, stop
                if distance <= k:
                    print("Duplicate found within k!")
                    print("Result: True")
                    return True
                    break

            else:
                print(f"First time seeing {num}")

            print(f"Updating seen[{num}] = {i}")

            seen[num] = i

            print(f"Dictionary AFTER: {seen}")
            print()

        else:
            print("No duplicates found within k.")
            print("Result: False")
            return False


print("=" * 30)
print("<>" * 15)
print("=" * 30, "\n")
print("Example 1")
example_1 = Solution()
print("Input: nums = [1, 9, 9, 1, 1], k = 1")
print(f"Output: {example_1.containsNearbyDuplicate([1, 9, 9, 1, 1], 1)} \n")

print("=" * 30)
print("<>" * 15)
print("=" * 30, "\n")
print("Example 2")
example_2 = Solution()
print("Input: nums = [1,2,3,1], k = 3")
print(f"Output: {example_2.containsNearbyDuplicate([1, 2, 3, 1], 3)} \n")


print("=" * 30)
print("<>" * 15)
print("=" * 30, "\n")
print("Example 3")
example_3 = Solution()
print("Input: nums = [1,0,1,1], k = 1")
print(f"Output: {example_3.containsNearbyDuplicate([1, 0, 1, 1], 1)} \n")


print("=" * 30)
print("<>" * 15)
print("=" * 30, "\n")
print("Example 4")
example_4 = Solution()
print("Input: nums = [1,2,3,1,2,3], k = 2")
print(f"Output: {example_4.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)} \n")
