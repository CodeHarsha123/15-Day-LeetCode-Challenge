class Solution(object):
    def isAnagram(self, s, t):
        s1 = sorted(s)
        t1 = sorted(t)
        return s1==t1       