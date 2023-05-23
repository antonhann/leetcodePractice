# def canSum(target, nums, memo = {}):
#     if target == 0:
#         return True
#     if target < 0:
#         return False
#     if target in memo:
#         return memo[target]
#     for i in nums:
#         rem = target - i   
#         memo[target] = canSum(rem, nums,memo)
#         if memo[target]:
#             return True
#     return False
def canSum(target, nums):
    dp = [False] * (target + 1)
    dp[0] = True
    for i in range(target):
        if dp[i] == True:
            for j in nums:
                if i + j <= target:
                    dp[i + j] = True
    return dp[target]
        
print(canSum(7,[2,3]))
print(canSum(7,[5,3,4,7]))
print(canSum(7,[2,4]))
print(canSum(300,[7,14]))