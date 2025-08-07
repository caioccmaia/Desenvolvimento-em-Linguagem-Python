#desenvolvimento
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k = 0
        for i in s[::-1]:
            if i != " ":
                k += 1
            elif k > 0:
                return k
        return k

#Modelo pythonico

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])
