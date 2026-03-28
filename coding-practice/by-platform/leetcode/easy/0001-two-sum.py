import enum


class Solution:
    # Brute Force Approach
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Thoughts
        ---------
        #Need to do nested for loop
        n = len(nums)
        Outer loop: i=0; n-1
            Inner loop: j=i+1; n
                if sum nums[i] + nums[j] == target
                    return [i, j] # can return the answer in any order.

        Complexity
        ----------
        Time complexity: O(n^2)
        Space complexity: O(1)
        """
        n = len(nums)
        for i in range(0, n-1):
            for j in range(i+1, n):
                check = nums[i] + nums[j]
                if check == target:
                    return [i, j]

    # With Hint 2 & 3
    def twoSum_v2(self, nums: List[int], target: int) -> List[int]:
        f"""
        Thoughts
        ---------
        # Instead of searching through entire array for each element in outer loop, we use a dictionary to search whether the complement already (target - num) exists in the dictionary. If it does not exist, we then add the current element (key) and index (value) in to the dictionary.

        Also, the reason for using dictionary after checking is if the dictionary is created at the start before checking, we would face two issues
        1) override the index if same value appears twice (e.g., nums=[3,3], target=6, d={3:1})
        2) same value might get retrieved as well (e.g., nums=[3,2,4], target=6, d={3:0, 2:1, 4:2}return would be [0,0] when we loop through each item and check for complement in dictionary)

        Pseudocode
        ---------
        d = {}
        for i in range(0, n)
            num = nums[i]
            complement = target - num
            if complement in d:
                return [d[complement], i]
            else:
                d[num] = i

        Complexity
        ----------
        Time complexity: O(n)
        Space complexity: O(n)
        """

        d = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], i]
            else:
                d[num] = i