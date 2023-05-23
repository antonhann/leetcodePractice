# def canConstruct(target, words, memo= {}):
#     if target == "":
#         return True
#     if target in memo:
#         return memo[target]
#     memo[target] = False
#     for i in words:
#         rem = target[:len(i)]
#         if rem == i:
#             if canConstruct(target[len(i):],words):
#                 memo[target] = True
#                 return True
#     return memo[target]
def canConstruct(target, words):
    dp = [False] * (len(target) + 1)
    dp[0] = True
    for i in range(len(target) + 1):
        if dp[i] == True:
            for j in words:
                # print(i, len(j))
                # print(target[i:len(j) + i])
                if i + len(j) < len(target) + 1 and target[i:len(j) + i] == j:
                    dp[i + len(j)] = True
    
    return dp[len(target)]
print(canConstruct("skateboard", ["skate","board"]))
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e','ee','eee','eee','eeee','eeeeee','eeeeee','eeeeee','eeeee','eeeee']))
# def canConstruct(target, words):
#     if target == "":
#         return True
#     for i in words:
#         rem = target[:len(i)]
#         if rem == i:
#             if canConstruct(target[len(i):],words):
#                 return True
#     return False

# print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e','ee','eee','eee','eeee','eeeeee','eeeeee','eeeeee','eeeee','eeeee']))