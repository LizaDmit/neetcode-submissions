class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start = 0
        maxF = 0 
        maxL = 0

        for end in range(len(s)):

            if s[end] not in count:
                count[s[end]] = 0

            count[s[end]] += 1
            maxF = max(maxF, count[s[end]])

            curW = end - start + 1
            curK = curW - maxF

            if curK > k:
                count[s[start]] -= 1
                start += 1

            maxL = max(maxL, end - start + 1)

        return maxL    


            
