def picker(prices):

    # Kadane's works here, we initialize the max profit on -inf
    
    max_profit = float("-inf")
    curr = 0
    coordinates = []

    # we get all coordinates where j is after i to avoid the sell before buy

    for i in range(len(prices)):
        for j in range(i,len(prices)):
            profit = prices[j] - prices[i]
            # if the current profit is better than max, we update the max and replace the coordinates
            curr = max (profit,curr)
            if curr > max_profit:
                max_profit = max(max_profit,curr)
                coordinates = [i,j]
    return coordinates

