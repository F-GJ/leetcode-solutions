"""
Given an integer array nums, return all the triplets [nums[i],
nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

link : https://leetcode.com/problems/3sum/?envType=problem-list-v2&envId=array
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        print("\n========== STEP 1: SORT ARRAY ==========")
        print(f"BEFORE nums.sort(): {nums}")

        nums.sort()

        print(f"AFTER  nums.sort(): {nums}")

        # STEP 2: Initialize the results list
        triplets = []

        print("\n========== STEP 2: INITIALIZE RESULTS ==========")
        print(f"triplets = {triplets}")

        # Display the index and value of every element
        print("\n========== ARRAY INDEX & VALUE ==========")

        for idx, val in enumerate(nums):
            print(f"Index {idx}: Value {val}")

        # STEP 3: Start the outer loop
        # Each outer iteration selects ONE first number.
        # The inner while loop must finish before i moves forward.
        print("\n========== STEP 3: OUTER LOOP ==========")

        for i in range(len(nums) - 2):
            print(f"\n{'=' * 50}")
            print(f"OUTER ITERATION {i + 1}")
            print(f"{'=' * 50}")

            # The for loop automatically assigns the next index to i.
            print(f"FOR LOOP selected: i = {i}")
            print(f"Current first number: nums[{i}] = {nums[i]}")

            # STEP 4: Skip duplicate first numbers
            if i > 0 and nums[i] == nums[i - 1]:
                print("\nDUPLICATE FIRST NUMBER DETECTED")
                print(f"Current:  nums[{i}] = {nums[i]}")
                print(f"Previous: nums[{i - 1}] = {nums[i - 1]}")
                print("ACTION: continue")
                print("The rest of this outer iteration is skipped.")

                continue

            # STEP 5: Initialize the LEFT pointer
            print("\n----- INITIALIZE LEFT POINTER -----")
            print("RULE: left = i + 1")
            print(f"CALCULATION: {i} + 1 = {i + 1}")

            left = i + 1

            print(f"LEFT INITIALIZED: left = {left}")
            print(f"LEFT VALUE: nums[{left}] = {nums[left]}")

            # STEP 6: Initialize the RIGHT pointer
            print("\n----- INITIALIZE RIGHT POINTER -----")
            print("RULE: right = len(nums) - 1")
            print(f"CALCULATION: {len(nums)} - 1 = {len(nums) - 1}")

            right = len(nums) - 1

            print(f"RIGHT INITIALIZED: right = {right}")
            print(f"RIGHT VALUE: nums[{right}] = {nums[right]}")

            # This counter restarts for each new first number.
            inner_iteration = 0

            print("\n========== ENTER INNER WHILE LOOP ==========")
            print(f"LOOP CONDITION: left < right → {left} < {right}")

            # STEP 7: Search for the other two numbers
            while left < right:
                inner_iteration += 1

                print(f"\n{'-' * 50}")
                print(f"INNER ITERATION {inner_iteration} (OUTER i = {i})")
                print(f"{'-' * 50}")

                # Display all three current indices and values
                print("\nCURRENT POINTERS")
                print(f"i     = {i} → nums[{i}] = {nums[i]}")
                print(f"left  = {left} → nums[{left}] = {nums[left]}")
                print(f"right = {right} → nums[{right}] = {nums[right]}")

                # STEP 8: Calculate the sum
                total = nums[i] + nums[left] + nums[right]

                print("\nCALCULATE TOTAL")
                print(f"total = {nums[i]} + {nums[left]} + {nums[right]} = {total}")

                # STEP 9: If total equals zero, save the triplet
                if total == 0:
                    print("\nDECISION: total == 0")
                    print("A valid triplet was found.")

                    print(f"\nBEFORE triplets.append(): {triplets}")

                    triplets.append([nums[i], nums[left], nums[right]])

                    print(f"AFTER  triplets.append(): {triplets}")

                    # Move LEFT forward
                    print("\n----- UPDATE LEFT POINTER -----")
                    print(f"BEFORE left += 1: left = {left}")

                    left += 1

                    print(f"AFTER  left += 1: left = {left}")

                    if left < len(nums):
                        print(f"NEW LEFT VALUE: nums[{left}] = {nums[left]}")

                    # Move RIGHT backward
                    print("\n----- UPDATE RIGHT POINTER -----")
                    print(f"BEFORE right -= 1: right = {right}")

                    right -= 1

                    print(f"AFTER  right -= 1: right = {right}")

                    if right >= 0:
                        print(f"NEW RIGHT VALUE: nums[{right}] = {nums[right]}")

                    while left < right and nums[left] == nums[left - 1]:
                        print("\n----- DUPLICATE VALUE DETECTED -----")
                        print(f"nums[{left}] = {nums[left]}")
                        print(f"nums[{left - 1}] = {nums[left - 1]}")
                        print("These values are equal, so we skip this position.")
                        print(f"BEFORE left += 1: left = {left}")

                        left += 1

                        print(f"AFTER left += 1: left = {left}")

                    while left < right and nums[right] == nums[right + 1]:
                        print("\n----- DUPLICATE RIGHT DETECTED -----")
                        print(f"nums[{right}] == nums[{right + 1}]")
                        print(f"{nums[right]} == {nums[right + 1]}")

                        print(f"BEFORE right -= 1: right = {right}")

                        right -= 1

                        print(f"AFTER  right -= 1: right = {right}")
                # STEP 10: If total is negative, increase the sum
                elif total < 0:
                    print("\nDECISION: total < 0")
                    print("The sum is too small.")
                    print("ACTION: Move LEFT forward to try a larger number.")

                    print(f"\nBEFORE left += 1: left = {left}")

                    left += 1

                    print(f"AFTER  left += 1: left = {left}")

                    if left < len(nums):
                        print(f"NEW LEFT VALUE: nums[{left}] = {nums[left]}")

                # STEP 11: If total is positive, decrease the sum
                elif total > 0:
                    print("\nDECISION: total > 0")
                    print("The sum is too large.")
                    print("ACTION: Move RIGHT backward to try a smaller number.")

                    print(f"\nBEFORE right -= 1: right = {right}")

                    right -= 1

                    print(f"AFTER  right -= 1: right = {right}")

                    if right >= 0:
                        print(f"NEW RIGHT VALUE: nums[{right}] = {nums[right]}")

                # Show whether the inner loop will run again
                print("\n----- CHECK WHILE CONDITION -----")
                print(f"left < right → {left} < {right} → {left < right}")

                if left < right:
                    print("RESULT: TRUE → Start another INNER iteration.")
                    print(f"IMPORTANT: i is still {i}.")
                else:
                    print("RESULT: FALSE → Exit the INNER while loop.")

            # This runs only after the inner while loop has finished
            print("\n========== INNER LOOP FINISHED ==========")
            print(f"Finished searching with i = {i}, nums[i] = {nums[i]}")
            print("Python now returns to the OUTER for loop.")

        # STEP 12: Display the final results
        print("\n========== FINAL RESULTS ==========")
        print(f"triplets = {triplets}")
