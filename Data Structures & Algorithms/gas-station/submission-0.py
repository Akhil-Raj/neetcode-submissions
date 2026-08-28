class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        resInd = 0
        currGas = gas[0] - cost[0]

        for i in range(1, len(gas)):
            if currGas < 0:
                resInd = i
                currGas = gas[i]
            else:
                currGas += gas[i]
                if resInd == i:
                    return resInd
            currGas -= cost[i]

        for i in range(len(gas)):
            if currGas < 0:
                resInd = i
                currGas = gas[i]
            else:
                currGas += gas[i]
                if resInd == i:
                    return resInd
            currGas -= cost[i]

        return -1