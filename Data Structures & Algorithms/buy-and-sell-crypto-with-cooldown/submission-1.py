class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp = [[0 for sell_day in range(len(prices))] for buy_day in range(len(prices))] # maximum profit, if last bought on buy_day and sold on sold_day. Ignore if buy_day > sold_day.
        auxMaxArray = [0 for sell_day in range(len(prices))] # maximum profit if last sold on sell_day

        auxMax = 0 # maximum profit if last sold atleast 2 days before buy_day

        res = 0

        for buy_day in range(min(2, len(prices))):
            for sell_day in range(buy_day + 1, len(prices)):
                mp[buy_day][sell_day] = prices[sell_day] - prices[buy_day]
                auxMaxArray[sell_day] = max(auxMaxArray[sell_day], mp[buy_day][sell_day])       
                res = max(res, mp[buy_day][sell_day])

        for buy_day in range(2, len(prices)):
            auxMax = max(auxMax, auxMaxArray[buy_day - 2])
            for sell_day in range(buy_day + 1, len(prices)):
                mp[buy_day][sell_day] = auxMax + (prices[sell_day] - prices[buy_day])
                auxMaxArray[sell_day] = max(auxMaxArray[sell_day], mp[buy_day][sell_day])       
                res = max(res, mp[buy_day][sell_day])
        # print(mp)
        return res