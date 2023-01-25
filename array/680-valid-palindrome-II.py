def isPalindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            skipL, skipR = s[start+1:end+1], s[start, end]
            return (skipL == skipL[::-1] or skipR == skipR[::-1])
    return True
print(isPalindrome("abca"))
print(isPalindrome("abc"))
print(isPalindrome("aba"))