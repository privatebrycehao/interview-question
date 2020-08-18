# Link =>>> https://leetcode.com/problems/search-in-rotated-sorted-array
# Given an integer array nums sorted in ascending order, and an integer target.

# Suppose that nums is rotated at some pivot unknown to you beforehand (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You should search for target in nums and if you found return its index, otherwise return -1.
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 用到二分模板，但是这题的重点是找到MID，之后如何切，左点和右点
# 由题意我们得知，这个被分割的数组，是由两个单调递增的数组组成，且R数组所有的数字都比L数组最小的数字小
# 这样我们可以找到左右以后，用二分找到target
class Solution:
    def search(self, nums, target):
        if not nums:
            return -1 
        l,r = 0, len(nums) -1 
        while l+1 < r:
            mid = (l+r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] < nums[mid]: # 说明，l -> mid 之间是持续递增
                if nums[l]<= target< nums[mid]: # 说明， l-> mid-> m 之间
                    r = mid
                else: # 说明， target 再mid右边
                    l = mid 
            else: # 说明 l, mid是在左右两边
                if nums[mid] <= target<= nums[r]: # 说明 ，target在 mid 和r之间
                    l = mid
                else:
                    r = mid
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        return -1
Solution.search([4,5,6,7,0,1,2], 0)


