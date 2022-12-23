# Traverse from 1 to min(a,b).
# And check if i is divisible by both a and b.
# If yes store it in the answer.
# Find the maximum value of i which divides both a and b.
def gcd(a,b):
    ans = 0
    for i in range(1, min(a, b)):
        if a%i == 0 and b%i == 0:
            ans = i
    return ans
x = gcd(9,21)
print(x)
#Time Complexity : O(n)
#Space Complexity : O(1)