def strStr(haystack, needle):
    if haystack.__contains__(needle):
        return haystack.index(needle)
    else:
        return -1
print(strStr("sadbutsad", "sad"))