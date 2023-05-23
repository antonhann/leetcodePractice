def grid(i, j):
    dp = [[0 for x in range(j + 1)] for y in range(i + 1)]
    dp[1][1] = 1
    for i in range(len(dp)):
        for j in range(len(dp)):
            if j < len(dp[0]) - 1:
                dp[i][j + 1] += dp[i][j]
            if i < len(dp) - 1:
                dp[i + 1][j]  += dp[i][j]
    # print(dp)
    return dp[i][j]
print(grid(1,1))
print(grid(2,2))
print(grid(3,3))
print(grid(18,18))