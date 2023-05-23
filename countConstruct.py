# def countConstruct(target,words):
#     if target == "":
#         return 1
#     res = 0
#     for i in words:
#         rem = target[:len(i)]
#         if i == rem:
#             res += countConstruct(target[len(i):],words)
#     return res

# print(countConstruct("purple", ['purp','p','ur','le', 'purpl']))
# print(countConstruct("skateboard", ['bo','rd','ate','t','ska','sk','boar']))
# print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e','ee','eee','eee','eeee','eeeeee','eeeeee','eeeeee','eeeee','eeeee']))
# def countConstruct(target,words, memo = {}):
#     if target == "":
#         return 1
#     if target in memo:
#         return memo[target]
#     res = 0
#     for i in words:
#         rem = target[:len(i)]
#         if i == rem:
#             res += countConstruct(target[len(i):],words)
#     memo[target] = res
#     return memo[target]












def countConstruct(s, words):
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    for i in range(len(dp)):
        if dp[i] != 0:
            for j in words:
                if i + len(j) < len(s) + 1 and s[i:len(j) + i] == j:
                    dp[i + len(j)] += dp[i]
    # print(dp)
    return dp[len(s)]
print(countConstruct("skateboard", ["skate","board"]))
print(countConstruct("purple", ['purp','p','ur','le', 'purpl']))
print(countConstruct("skateboard", ['bo','rd','ate','t','ska','sk','boar']))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e','ee','eee','eee','eeee','eeeeee','eeeeee','eeeeee','eeeee','eeeee']))