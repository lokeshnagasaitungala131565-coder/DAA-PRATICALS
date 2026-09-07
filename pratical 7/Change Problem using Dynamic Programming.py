def min_coins(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1


# Input
coins = list(map(int, input("Enter coin values: ").split()))
amount = int(input("Enter amount: "))

# Output
result = min_coins(coins, amount)

if result == -1:
    print("Change cannot be made")
else:
    print("Minimum number of coins:", result)