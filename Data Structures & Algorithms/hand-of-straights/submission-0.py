class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        freq = [0 for i in range(1001)]
        for handNum in hand:
            freq[handNum] += 1
        
        for ind in range(len(freq)):
            if freq[ind] > 0:
                f = freq[ind]
                if ind + groupSize - 1 >= len(freq):
                    return False
                for subInd in range(ind, ind + groupSize):
                    freq[subInd] = freq[subInd] - f
                    if freq[subInd] < 0:
                        return False

        return True

# hand=[1,2,3,3,4,5,6,7]
# groupSize=4
# freq = [0, 1, 1, 2, 1, 1, 1, 1]
## ind = 0, 1
## subInd = [1, 4]
## freq = [0, 0, 0, 1, 0, 1, 1, 1]
## ind = 2, 3
## subInd = [3, 6]
## freq = [0, 0, 0, ]