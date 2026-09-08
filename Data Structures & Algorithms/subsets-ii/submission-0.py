class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        out = []


        def find_dups(nums, ind, arr):
            if ind >= len(nums):
                if sorted(arr.copy()) not in out:
                    out.append(sorted(arr.copy()))
                return
            
            # take ele
            arr.append(nums[ind])
            find_dups(nums, ind + 1, arr)
            # don't take ele
            arr.pop()
            find_dups(nums, ind + 1, arr)
        
        find_dups(nums, 0, [])

        return out