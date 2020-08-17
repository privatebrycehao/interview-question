# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:
# nums1 = [1, 3] nums2 = [2]
# The median is 2.0

# Example 2:
# nums1 = [1, 2] nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5

# 转换为findkth, 奇数find k // 2 + 1, 偶数，找到 K //2 和 K//2 + 1 再除以 2， 取float

# 例子： A：[2,3,6,7,9] b: [1,4,8,10] find 5th.
# 取K的一半(这样可以保证a+b 不大于K)
# k//2 =>>> 2, A的第二个数字是3， B的第二个数字是4， 3 小于4,所以， A的前两个数字必定再前4个之内,前五个数字取到了（2,3）, K变成 找到剩下前五个中的3个
# A:[6,7,9] b: [1,4,8,10] K = 3
# k //2  =》》》 1， A的第一个数字是 6, B的第一个数字是1， 1小于6，所以 1必定再前五个中，前五个数字（2,3,1） K变成找到剩下前五个中的2个
# A：[6,7,9] b:[4,8,10], K = 2
# k //2  =》》》 1， A的第一个数字是 6, B的第一个数字是4， 4小于6，所以 4必定再前五个中，前五个数字（2,3,1,4） K变成找到剩下前五个中的1个
# A: [6,7,9], b: [8,10] k = 1
# 找一个， 所以找寻 min(A[0],B[0]), =>>>>> 6, 第五个数字就是6
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2:
            return self.findkth(nums1, nums2, l//2+1)
        else:
            return (self.findkth(nums1, nums2, l//2) + self.findkth(nums1, nums2, l//2+1)) / 2
    def findkth(self,nums1, nums2, k):
        if len(nums1) > len(nums2):
            return self.findkth(nums2, nums1,k)
        if not nums1:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0], nums2[0])
        pa = min(k//2, len(nums1))
        if nums1[pa-1] < nums2[pa-1]:
            return self.findkth(nums1[pa:], nums2, k-pa)
        else:
            return self.findkth(nums1, nums2[pa:], k-pa)
