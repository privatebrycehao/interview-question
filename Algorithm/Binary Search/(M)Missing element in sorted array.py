# 1060. Missing Element in Sorted Array
# Share
# Given a sorted array A of unique numbers, find the K-th missing number starting from the leftmost number of the array.

# Example 1:
# Input: A = [4,7,9,10], K = 1
# Output: 5
# Explanation: 
# The first missing number is 5.

# Example 2:
# Input: A = [4,7,9,10], K = 3
# Output: 8
# Explanation: 
# The missing numbers are [5,6,8,...], hence the third missing number is 8.

# Example 3:
# Input: A = [1,2,4], K = 3
# Output: 6
# Explanation: 
# The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

# 两种情况， 一种丢失的数字在数组最大值和最小值之间， 第二种情况，数组丢失 x个， 但是我们要找 x + m个， 直接返回 nums[-1] + missing的个数
# 第一种情况的二分， 如果在最大值和最小值之间，取mid，然后找mid到left丢失多少个数字，如果大于K的话， 答案在L和M之间， 如果小于K， 就说明 指针要找MID后面的数字

class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        if not nums or k == 0:
            return 0
        diff = nums[-1] - nums[0] + 1
        missing = diff - len(nums)
        if missing < k:
            return nums[-1] + k - missing
        l, r = 0, len(nums) - 1
        while l + 1< r:
            mid = (l+r) // 2
            missing = nums[mid] - nums[l] - (mid - l)
            if missing < k:
                l = mid
                k -= missing
            else:
                r = mid 
        return nums[l] + k