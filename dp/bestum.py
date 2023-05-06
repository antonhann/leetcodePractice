def bestSum(n, nums, memo = {}):
    if n == 0:
        return []
    if n < 0:
        return None
    if n in memo:
        return memo[n]
    shortest = None
    for i in nums:
        rem = n - i
        res = bestSum(rem, nums,memo)
        if res != None:
            combination = res + [i]
            if not shortest or len(combination) < len(shortest):
                shortest = combination
    memo[n] = shortest
    return memo[n]
    
print(bestSum(4,[1,2]))
print(bestSum(8,[2,3,5]))
print(bestSum(8,[1,4,5]))
print(bestSum(100,[1,2,5,25]))