def knapsack(values, weights, capacity):
    n = len(values)

    # Create DP table
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],
                    dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Input
n = int(input("Enter the number of items: "))

values = []
weights = []

print("\nEnter value and weight of each item:")

for i in range(n):
    value = int(input(f"Value of item {i + 1}: "))
    weight = int(input(f"Weight of item {i + 1}: "))
    values.append(value)
    weights.append(weight)

capacity = int(input("\nEnter the knapsack capacity: "))
# Calculate maximum value
result = knapsack(values, weights, capacity)

# Output
print("Maximum value:", result)