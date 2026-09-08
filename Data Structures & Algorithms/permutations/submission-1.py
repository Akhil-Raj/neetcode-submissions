class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []

        def get_perms(arr, nums):
            flag = False
            for ind in range(len(nums)):
                if nums[ind] != -100:
                    flag = True
                    val = nums[ind]
                    arr.append(nums[ind])
                    nums[ind] = -100
                    get_perms(arr, nums)
                    nums[ind] = val
                    arr.pop()
            
            if not flag:
                out.append(arr.copy())

        get_perms([], nums)
        return out