# Link => https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
# 和33 题思路一样， 只是加入了重复，如果去重, while 循环直接左+1到不重复为止 
#  如何找到重复， 找左边是否有和mid的数值是一样的，也就是切换点，如果有一样的l+1 防止， [1,1,1,1,1,1,1,1,1,1,0] 这样的数组出现
class Solution:
    def search(self,nums, target):
            l, r = 0, len(nums)-1
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] == target:
                    return True
                while l < mid and nums[l] == nums[mid]: # tricky part
                    l += 1
                # the first half is ordered
                if nums[l] <= nums[mid]:
                    # target is in the first half
                    if nums[l] <= target < nums[mid]:
                        r = mid - 1
                    else:
                        l = mid + 1
                # the second half is ordered
                else:
                    # target is in the second half
                    if nums[mid] < target <= nums[r]:
                        l = mid + 1
                    else:
                        r = mid - 1
            return False
