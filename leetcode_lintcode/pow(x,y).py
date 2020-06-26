class Solution:
    """
    @param x {float}: the base number
    @param n {int}: the power number
    @return {float}: the result
    """
    def myPow(self, x: float, n: int) -> float:
        if n == 0 :
             return 1
        if n< 0 :
            x = 1 // x
            n = - n
        ans = 1
        tmp = x
        while n!=0 :
            if n % 2 == 1:
                ans *= tmp
            tmp *= tmp
            n = n // 2
        return ans
