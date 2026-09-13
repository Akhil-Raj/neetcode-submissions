class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lcss = [[0 for i in range(len(text2))] for j in range(len(text1))]
        lcss[0][0] = 1 if text1[0] == text2[0] else 0

        for row in range(1, len(text1)):
            lcss[row][0] = 1 if text1[row] == text2[0] else lcss[row - 1][0]

        for col in range(1, len(text2)):
            lcss[0][col] = 1 if text1[0] == text2[col] else lcss[0][col - 1]
        
        for row in range(1, len(text1)):
            for col in range(1, len(text2)):
                if text1[row] == text2[col]:
                    lcss[row][col] = lcss[row - 1][col - 1] + 1
                else:
                    # if text1[row] is part of lcss
                    text2Ind = text2[:col].rfind(text1[row])
                    val1 = lcss[row][text2Ind] if text2Ind != -1 else 0
                    
                    # if text2[col] is part of lcss
                    text1Ind = text1[:row].rfind(text2[col])
                    val2 = lcss[text1Ind][col] if text1Ind != -1 else 0

                    # neither is part of lcss
                    val3 = lcss[row - 1][col - 1]

                    val = max(val1, val2, val3)

                    lcss[row][col] = val
        # print(lcss)
        return lcss[-1][-1]