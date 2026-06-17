class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        cleaned=""
        for ch in s:
            if ch.isalnum():
                cleaned+=ch
        rev=cleaned[::-1]
        return cleaned==rev
        