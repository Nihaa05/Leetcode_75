class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {"a","e","i","o","u"}
        count = 0
        maxcount = 0
        i = 0

        for j in range(len(s)):
            if s[j] in vowels:
                count += 1
            if j >= k-1:
                maxcount = max(count,maxcount)
                if s[i] in vowels:
                    count -= 1
                i+= 1
        return maxcount
