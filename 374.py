# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while True:
            mid = (lo + hi) / 2
            if guess(mid) == 1:
                if hi - lo == 1:
                    return hi
                lo = mid
                continue
            if guess(mid) == -1:
                hi = mid
                continue
            if guess(mid) == 0:
                return mid

