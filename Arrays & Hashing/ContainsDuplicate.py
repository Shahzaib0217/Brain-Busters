class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        # set only contains unique elements
        st = set()
        for i in range(n):    
            if nums[i] in st:
                return True
            else:
                st.add(nums[i])
        return False