class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort appraoch  
        
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        # count frequeny and store in a dic
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        # storing same freq elements together in array of arrays
        for num, cnt in count.items():
            freq[cnt].append(num)
            
        # returing top k elements
        res = []
        # range(start, stop, step)
        # Starting from the end cuz the highest freq element is at the end
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
                