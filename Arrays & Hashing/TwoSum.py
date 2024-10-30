class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # any 2 indexes sum = target
        # t=23 a=20 b=3 t-a == b

        length = len(nums)

        s = {}

        for i in range(length):
            # if nums[i] is in the set
            if nums[i] in s.keys():
                # if yes return index in the set and i [set_ind, i]
                return [s[nums[i]], i]
            else:
                # comp = t-nums[i]
                comp = target - nums[i]
                # insert comp & i in set
                s[comp] = i
