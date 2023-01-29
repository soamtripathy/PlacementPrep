def printNto1(i, n):
    if i < 1:
        return
    print(i)
    printNto1(i-1,n )
printNto1(10, 10)
# #Using BackTracking
def printNto1(i, num):

    if i > num:
        return 
    printNto1(i+1, num)
    print(i)
printNto1(1, 5)
