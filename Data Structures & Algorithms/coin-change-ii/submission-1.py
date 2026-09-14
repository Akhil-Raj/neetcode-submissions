class Solution:
    def change(self, target: int, coins: List[int]) -> int:
        noc = [[-1 for mdi in range(len(coins))] for t in range(target + 1)]
        coins.sort()

        def find_noc(target, mdi):
            if target == 0:
                return 1
            if noc[target][mdi] != -1:
                return noc[target][mdi]
            
            noc[target][mdi] = 0
            for ind in range(mdi, -1, -1):
                if target >= coins[ind]:
                    noc[target][mdi] += find_noc(target - coins[ind], ind)
            
            return noc[target][mdi]
        
        noc[target][len(coins) -1] = find_noc(target, len(coins) - 1)
        # print(noc)
        return noc[target][len(coins) - 1]