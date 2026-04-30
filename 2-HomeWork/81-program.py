class Solution:
    def sortString(self, s):
        # Step 1: Count frequency
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: Sort based on (frequency, character)
        sorted_chars = sorted(freq.items(), key=lambda x: (x[1], x[0]))

        # Step 3: Build result
        result = ""
        for ch, f in sorted_chars:
            result += ch * f

        return result
    
s = "geeksforgeeks"

obj = Solution()
print(obj.sortString(s))