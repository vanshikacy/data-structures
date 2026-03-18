def maxProfit(prices):
    maxprofit=0
    l=0 #first buy day 

    for r in range(1, len(prices)):
        if prices[r]<prices[l]: 
            #i.e. a better buy day is at right
            l=r 
        else:
            profit=prices[r]-prices[l]
            maxprofit=max(profit, maxprofit)
        
    return maxprofit

if __name__ == "__main__":
    prices = list(map(int, input("Enter prices separated by space: ").split()))
    
    result = maxProfit(prices)
    print("Max Profit:", result)