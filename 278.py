# 一次通过
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = n
        t = 1
        while True:
            while isBadVersion(i):
                i -= t
                t *= 2
            if t == 2:
                return i + 1
            i += t / 2
            t = 1

