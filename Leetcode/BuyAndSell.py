def BuySell(prices):
    profit=0
    current_price=prices[0]
    for i in prices[1:]:
        if current_price>i:
            current_price=i
        profit=max(profit,i-current_price)
    return profit

print(BuySell([7,1,5,3,6,4]))