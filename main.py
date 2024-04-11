from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    num_indices = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_indices:
            return [num_indices[complement], i]
        num_indices[num] = i
    return []

# Example usage:
# print(twoSum([2, 7, 11, 15], 9))  # Output: [0, 1]

# Example 1
nums1 = [2, 7, 11, 15]
target1 = 9
print("Example 1:")
print("Input:", nums1, target1)
print("Output:", twoSum(nums1, target1))  # Expected output: [0, 1]

# Example 2
nums2 = [3, 2, 4]
target2 = 6
print("\nExample 2:")
print("Input:", nums2, target2)
print("Output:", twoSum(nums2, target2))  # Expected output: [1, 2]

# Example 3
nums3 = [3, 3]
target3 = 6
print("\nExample 3:")
print("Input:", nums3, target3)
print("Output:", twoSum(nums3, target3))  # Expected output: [0, 1]
