
exports.picker = function(prices) {

    let max_profit = -Infinity
    let curr = 0
    let coordinates = []

    for (let i = 0; i < prices.length; i++){
        for (let j = i; j < prices.length; j++){
            profit = prices[j] - prices[i]
            curr = Math.max(profit,curr)
            if (curr > max_profit){
                max_profit = Math.max(max_profit,curr)
                coordinates = [i,j]
            }
        }
    }
    return coordinates
}
