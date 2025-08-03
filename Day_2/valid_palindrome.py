class Solution(object):
    def isPalindrome(self, s):
        empty = ""
        s=s.lower()
        for i in s:
            if i.isalnum():
                empty+=i
        return empty==empty[::-1]