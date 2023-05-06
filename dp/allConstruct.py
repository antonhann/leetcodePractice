def allConstruct(target, words):
    if target == "":
        return [[]]
    res = []
    for i in words:
        rem = target[:len(i)]
        if rem == i:
            ans = allConstruct(target[len(i):],words)
            for j in range(len(ans)):
                ans[j].append(i)
            res += ans
    return res
            
print(allConstruct("purple", ['purp','p','ur','le', 'purpl']))

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
            
# print(allConstruct("purple", ['purp','p','ur','le', 'purpl']))