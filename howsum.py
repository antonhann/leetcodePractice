# def howSum(n, arr, memo = {}):
#     if n == 0:
#         return []
#     if n < 0:
#         return None
#     if n in memo:
#         return memo[n]
#     for i in arr:
#         rem = n - i
#         remResult = howSum(rem, arr,memo)
#         if remResult != None:
#             memo[n] = remResult + [i]
#             return memo[n]
#     memo[n] = None
#     return None
def howSum(target, nums):
    dp = [None] * (target + 1)
    dp[0] = []
    for i in range(target + 1):
        if dp[i] != None:
            for j in nums:
                if i + j < target + 1:
                    dp[i + j] = dp[i] + [j]
    # print(dp)
    return dp[target]
print(howSum(7,[2,3]))
print(howSum(8,[3,5,2]))
print(howSum(4,[1,2]))