# 题目很简单， 计算除法，不可以用 乘法和除法 还有取余, 如果超过integer界限返回 2*31 - 1
# 思路是二分， 利用减法
# a << 1 等于 a * 2
# a<<b 等于 a*(2**b)
# 难点， 要对 除数 做位运算， 乘2的对数
# sample: 100/ 9
# 9<<0: 9
# 9<<1: 18
# 9<<2: 36
# 9<<3: 72
# 9<<3: 144
# 取 1<<3 ==> 8, 还剩 100-72 =》 28
# 可以看出 9<<2最大， 18， 还剩28-18， 10
# 9<<0最大， 还剩1，不能再取
## ans = 1<<3 + 1<<2+1<<0 = 8+2+1 ==> 11
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        is_negative = False
        # 是否负数
        if (divisor < 0 or dividend < 0) and not (divisor < 0 and dividend < 0):
            is_negative = True
        #取正
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            shift = 0
            while dividend >= divisor << (shift+1):
                shift += 1
            ans += 1 << shift
            dividend -= (divisor<< shift)
        if is_negative:
            ans = 0- ans
        if ans< -2 **31 -1 or ans> 2**31 - 1:
            return 2**31 -1
        return ans