class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            # [-4,-1,-1,0,1,2]
            #  No need to check positive values again
            if a > 0:
                break
            
            # avoiding duplicates
            if i > 0 and a == nums[i - 1]:
                continue

            # incase of i=4, finding the 2 nums which make -4. Using 2 pointers approach.  
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # skip all duplicate element
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                        
        return res