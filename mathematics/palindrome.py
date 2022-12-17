def palindrome(num):
    reversedNum = 0
    while num > 0:
        lastDigit = num%10
        num = num//10
        reversedNum = reversedNum*10 + lastDigit
    return reversedNum
x = palindrome(1043) 
print(x)
