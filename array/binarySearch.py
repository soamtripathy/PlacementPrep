list = [1, 5, 6, 8, 11, 34, 25]
def binarySearch(num):
    if num in list:
        return (f"{num} is present.")
    else:
        return ("You're on wrong list")
x = int(input("Enter the number:"))
y = binarySearch(x)
print(y)
