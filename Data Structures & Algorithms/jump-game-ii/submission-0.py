class Solution:
    def jump(self, nums: List[int]) -> int:
        auxArr = [0]
        maxIndLeft = 0
        for ind in range(1, len(nums)):
            if ind + nums[ind] > maxIndLeft + nums[maxIndLeft]:
                maxIndLeft = ind
            auxArr.append(maxIndLeft)
        
        minNumOfJumps = 0

        currInd = 0
        while(currInd < len(nums) - 1):
            currInd = auxArr[currInd] + nums[auxArr[currInd]]
            minNumOfJumps += 1
        
        return minNumOfJumps