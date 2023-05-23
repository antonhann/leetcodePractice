# def bestSum(n, nums, memo = {}):
#     if n == 0:
#         return []
#     if n < 0:
#         return None
#     if n in memo:
#         return memo[n]
#     shortest = None
#     for i in nums:
#         rem = n - i
#         res = bestSum(rem, nums,memo)
#         if res != None:
#             combination = res + [i]
#             if not shortest or len(combination) < len(shortest):
#                 shortest = combination
#     memo[n] = shortest
#     return memo[n]
def bestSum(target, nums):
    dp = [None] * (target + 1)
    dp[0] = []
    for i in range(target):
        if dp[i] != None:
            for j in nums:
                if i + j < target + 1:
                    new = dp[i] + [j]
                    if not dp[i + j] or len(new) < len(dp[i + j]):
                        dp[i + j] = new
    # print(dp)
    return dp[target]
print(bestSum(4,[1,2]))
print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))
print(bestSum(100,[1,2,5,25]))