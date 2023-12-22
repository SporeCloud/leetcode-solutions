class Solution:
    def myPow(self, x: float, n: int) -> float: #apparently this beat 97% of other cases for runtime, but it's very memory inefficient
        if n == 0: return 1
        elif n == 1: return x
        elif n == -1: return 1/x

        z = self.myPow(x,n//2)
        if n%2 == 0:
            return z*z
        elif n%2 == 1:
            return x*z*z
