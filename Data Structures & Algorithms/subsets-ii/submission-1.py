class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []


        def find_dups(nums, ind, arr):
            if ind >= len(nums):
                s = sorted(arr.copy())
                if s not in out:
                    out.append(s)
                return
            
            # take ele
            arr.append(nums[ind])
            find_dups(nums, ind + 1, arr)
            # don't take ele
            arr.pop()
            find_dups(nums, ind + 1, arr)
        
        find_dups(nums, 0, [])

        return out