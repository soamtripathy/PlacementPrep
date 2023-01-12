def find_min_sum(num):
    # Convert the number to a string and sort the digits
    s = "".join(sorted(str(num)))
    n = len(s)

    # Take the first two digits and the last two digits from the sorted string
    a = "".join([s[0],s[n-1]])
    b = "".join([s[1], s[n-2]])
    

    # Convert the substrings to integers and return the sum
    return int(a) + int(b)

# Test the function
print(find_min_sum(4296))  # Output: 75