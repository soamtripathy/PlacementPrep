def plusOne(digits):
        num = int("".join(map(str, digits)))
        num = num+1
        res = []
        for i in str(num):
            res.append(int(i))
        return res
print(plusOne([1,2,3]))
print(plusOne([9, 9]))