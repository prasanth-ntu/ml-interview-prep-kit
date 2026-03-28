from typing import List


class Solution:
    # Attempt 1: Brute force
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Thoughts
        --------
        Let's create an array/list where we will store the unique elements.
        Do a for loop of each element and check if it already exists in the unique element, and if it exists, we return True
        After the for loop, we return false


        Pseudocode
        -----------
        unique_nums = []
        for num in nums:
            if num in unique_nums:
                return True
            else:
                unique_nums.append(num)
        return False


        Complexity
        ----------
        Time Complexity: O(n²) - `in` on list is O(n), done n times
        Space Complexity: O(n)


        LeetCode Submission Result
        ------------------
        Time Limit Exceeded
        70 / 77 testcases passed
        """
        unique_nums = []
        for num in nums:  
            if num in unique_nums: # Time complexity: O(n) for each num
                return True
            else:
                unique_nums.append(num)
        return False

    # Attempt 2: Using a set for O(1) lookup
    def containsDuplicate_v2(self, nums: List[int]) -> bool:
        """
        Thoughts
        --------
        Same logic as Attempt 1, but use a set instead of a list.
        Sets use hash tables internally, giving O(1) average lookup time.

        Complexity
        ----------
        Time Complexity: O(n) - single pass, O(1) lookup per element
        Space Complexity: O(n) - storing up to n elements in the set

        Thoughts post submission
        ------------------------
        Ideally, we need to use set/dict for O(1) lookup as it's backed by hash table, instead of list which is O(n)
    
        """
        unique_nums = set()  # Use set() not {} - empty {} creates a dict!
        for num in nums:
            if num in unique_nums: # O(1) lookup
                return True
            else:
                unique_nums.add(num)
        return False

    # Attempt 2b: One-liner 
    def containsDuplicate_v2b(self, nums: List[int]) -> bool:
        """
        Thoughts
        --------
        Same logic as above, expcet use Set all the way
        """

        return len(nums) != len(set(nums))


if __name__ == "__main__":
    solution = Solution()

    # Test cases from LeetCode
    test_cases = [
        # (input, expected_output, description)
        ([1, 2, 3, 1], True, "Example 1: duplicate 1 at indices 0 and 3"),
        ([1, 2, 3, 4], False, "Example 2: all elements distinct"),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True, "Example 3: multiple duplicates"),
    ]

    print("Testing containsDuplicate (brute force - O(n²)):")
    print("-" * 50)
    for nums, expected, description in test_cases:
        result = solution.containsDuplicate(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print()

    print("\nTesting containsDuplicate_v2 (set - O(n)):")
    print("-" * 50)
    for nums, expected, description in test_cases:
        result = solution.containsDuplicate_v2b(nums)
        status = "✓" if result == expected else "✗"
        print(f"{status} {description}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print()
