class Solution:
    def fillMinMaxDict(self, s, minMaxDict):
        for ind in range(len(s)):
            if s[ind] in minMaxDict:
                minMaxDict[s[ind]][1] = ind
            else:
                minMaxDict[s[ind]] = [ind, -1]
        
    def partitionLabels(self, s: str):
        minMaxDict = {}
        self.fillMinMaxDict(s, minMaxDict)
        sizes = []
        ind = 0
        while ind < len(s):
            if minMaxDict[s[ind]][1] == -1:
                sizes.append(1)
                ind += 1
                continue
            end = minMaxDict[s[ind]][1]
            stInd = ind
            while(ind <= end):
                if minMaxDict[s[ind]][1] != -1 and minMaxDict[s[ind]][1] > end:
                    end = minMaxDict[s[ind]][1]
                ind += 1
            sizes.append(end + 1 - stInd)

        return sizes