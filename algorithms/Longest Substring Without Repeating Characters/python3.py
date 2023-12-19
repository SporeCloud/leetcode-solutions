class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_index = {}
        max_len = 0
        window_start = 0
        for x,y in enumerate(s):
            if y in last_index:
                window_start=max(window_start,last_index[y]+1)
            max_len=max(max_len,x-window_start+1)
            last_index[y] = x
        return max_len
