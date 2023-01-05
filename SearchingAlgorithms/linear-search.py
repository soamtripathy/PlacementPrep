# def linearSearch(num, k):
#     for i in range(len(num)):
#         if num[i] == k:

#             return i
# print(linearSearch([1, 3, 6, 9, 8], 9))
"""--------------------------------------------------"""


def linearSearch(num, k):
    if k in num:
        return num.index(k)
print(linearSearch([1, 3, 6, 9, 8], 9))

