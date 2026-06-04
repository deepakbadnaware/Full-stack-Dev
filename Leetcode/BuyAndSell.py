def BuySell(prices):
    # maxxi=0
    # n=len(prices)
    # for i in range(n-1):
    #     for j in range(i+1,n):
    #         if prices[j]>prices[i]:
    #             profit=prices[j]-prices[i]
    #             maxxi=max(profit,maxxi) 
    # return maxxi
    profit=0
    minimum=float('inf')
    n=len(prices)
    for i in range(n):
        minimum=min(minimum,prices[i])
        profit=max(profit,prices[i]-minimum)
    return profit



print(BuySell([7,1,5,3,6,4]))