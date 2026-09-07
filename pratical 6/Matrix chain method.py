def matrix_chain_order(p):
    n = len(p) - 1

    # dp[i][j] = minimum scalar multiplications
    dp = [[0 for _ in range(n)] for _ in range(n)]

    # Chain length
    for length in range(2, n + 1):

        for i in range(n - length + 1):
            j = i + length - 1

            dp[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i] * p[k + 1] * p[j + 1]
                )

                dp[i][j] = min(dp[i][j], cost)

    return dp


# Matrix dimensions
# A1 = 10 x 30
# A2 = 30 x 5
# A3 = 5 x 60
p = [10, 30, 5, 60]

dp = matrix_chain_order(p)

print("DP Table:")

for row in dp:
    print(row)

print("\nMinimum number of scalar multiplications:", dp[0][len(p) - 2])