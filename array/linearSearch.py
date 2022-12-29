#Advance python using if else
list = [1, 5, 6, 8, 11, 34, 25]
def linearSearch(num):
    if num in list:
        return (f"{num} is present.")
    else:
        return ("You're on wrong list")
x = int(input("Enter the number:"))
y = linearSearch(x)
print(y)
'''------------------------------------------------------------------------------'''
#traditional method of linear search
def linearSearch(num):
    for i in list:
        if num == i:
            return (f"{num} is present.")
        
    return ("You're wrong list")
x = int(input("Enter the number:"))
y = linearSearch(x)
print(y)