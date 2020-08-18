# 34. Find First and Last Position of Element in Sorted Array
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# 两次 Binary Search, 找左右，没有什么难度
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        if len(nums) < 1:
            return [-1,-1]
        l,r = 0, len(nums) -1 
        while l+1<r:
            mid = (l+r) // 2
            if nums[mid] >= target:
                r = mid
            if nums[mid] < target:
                l = mid
        if nums[r] == target:
            ans[0] = r
        if nums[l] == target:
            ans[0] = l
        if ans[0] == -1:
            return ans
        l, r = 0, len(nums) -1 
        while l+1<r:
            mid = (l+r) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid
        if nums[l] == target:
            ans[1] = l
        if nums[r] == target:
            ans[1] = r
        return ans
                