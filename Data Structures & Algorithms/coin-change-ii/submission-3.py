class Solution:
    def change(self, target: int, coins: List[int]) -> int:
        noc = [[-1 for mdi in range(len(coins))] for t in range(target + 1)]
        coins.sort()

        def find_noc(target, mdi):
            if target == 0:
                return 1
            if mdi < 0 or target < 0:
                return 0
            if noc[target][mdi] != -1:
                return noc[target][mdi]
            
            noc[target][mdi] = 0
            # if taking mdi's val, and can take it again
            if target >= coins[mdi]:
                noc[target][mdi] += find_noc(target - coins[mdi], mdi)
            # if not taking mdi's val
            noc[target][mdi] += find_noc(target, mdi - 1)
            
            return noc[target][mdi]
        
        noc[target][len(coins) -1] = find_noc(target, len(coins) - 1)
        # print(noc)
        return noc[target][len(coins) - 1]