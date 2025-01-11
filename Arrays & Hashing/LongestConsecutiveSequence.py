class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Dict Initailized with 0's
        mp = defaultdict(int)
        res = 0

        # nums = [100, 4, 200, 1, 3, 2] 
        for num in nums:
            if not mp[num]:
                # mp[100] = mp[99] + mp[101] +1 
                # mp[100] = 1
                mp[num] = mp[num - 1] + mp[num + 1] + 1
                # mp[100 - mp[99]] = 1
                mp[num - mp[num - 1]] = mp[num]
                # mp[100 + mp[101]] = 1
                mp[num + mp[num + 1]] = mp[num]
                res = max(res, mp[num])
        return res