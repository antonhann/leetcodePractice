def canSum(target, nums, memo = {}):
    if target == 0:
        return True
    if target < 0:
        return False
    if target in memo:
        return memo[target]
    for i in nums:
        rem = target - i   
        memo[target] = canSum(rem, nums,memo)
        if memo[target]:
            return True
    return False
print(canSum(300,[7,14]))