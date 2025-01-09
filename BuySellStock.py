class Solution:
    def maxProfit(self, prices):
        maxProfit = 0
        bestBuy = prices[0]

        for i in range(1, len(prices)):
            if prices[i] > bestBuy:
                maxProfit = max(maxProfit, prices[i] - bestBuy)
            bestBuy = min(bestBuy, prices[i])
        
        return maxProfit

def main():
    n = int(input("Enter the number of days: "))

    prices = []
   
    print("Enter the stock prices for each day: ")

    for i in range(n):
        price = int(input())
        prices.append(price)

    obj = Solution()
    iRet = obj.maxProfit(prices)
    print("The maximum profit is: ", iRet)

if __name__ == "__main__":
    main()
