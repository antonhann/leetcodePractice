# def allConstruct(target, words):
#     if target == "":
#         return [[]]
#     res = []
#     for i in words:
#         rem = target[:len(i)]
#         if rem == i:
#             ans = allConstruct(target[len(i):],words)
#             for j in range(len(ans)):
#                 ans[j].append(i)
#             res += ans
#     return res
            
# print(allConstruct("purple", ['purp','p','ur','le', 'purpl']))

#python refers to the return memo as a reference rather than a copy
# def allConstruct(target, words, memo = {}):
#     if target in memo:
#         return memo[target]
#     if target == "":
#         return [[]]
#     res = []
#     for i in words:
#         rem = target[:len(i)]
#         if rem == i:
#             ans = allConstruct(target[len(i):],words,memo).copy()
#             for j in range(len(ans)):
#                 ans[j].append(i)
#             res += ans
#     memo[target] = res
#     return res
def allConstruct(s, words):
    dp = [] * len(s) + 1
    dp[0] = [[]]
    for i in range(len(s) + 1):
        if dp[i] != []:
            for j in words:
                if i + len(j) < len(s) + 1 and s[i:len(j) + 1] == j:
                    for d in dp[0]:
print(allConstruct("purple", ['purp','p','ur','le', 'purpl']))