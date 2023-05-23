def fib(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2,len(dp)):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
print(fib(6))
print(fib(7))
print(fib(8))
print(fib(50))