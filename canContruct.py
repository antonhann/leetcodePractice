def canConstruct(target, words, memo= {}):
    if target == "":
        return True
    if target in memo:
        return memo[target]
    memo[target] = False
    for i in words:
        rem = target[:len(i)]
        if rem == i:
            if canConstruct(target[len(i):],words):
                memo[target] = True
                return True
    return memo[target] 

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