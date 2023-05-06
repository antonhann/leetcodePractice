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
def countConstruct(target,words):
    if target == "":
        return 1
    res = 0
    for i in words:
        rem = target[:len(i)]
        if i == rem:
            res += countConstruct(target[len(i):],words)
    return res

print(countConstruct("purple", ['purp','p','ur','le', 'purpl']))
print(countConstruct("skateboard", ['bo','rd','ate','t','ska','sk','boar']))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ['e','ee','eee','eee','eeee','eeeeee','eeeeee','eeeeee','eeeee','eeeee']))