# 非常令我惊叹的解决办法，既然结构相同，那就把结构相同的去掉，看还有没有剩余，利用zip函数把对应字符放在一起，用set去掉重复，判断长度是否相等即可。一行解决，真的牛逼
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s,t)))==len(set(s))==len(set(t))

print Solution().isIsomorphic("aaaaabbbbbcccccdddddeeeee","pppppqqqqqrrrrrsssssttttt")