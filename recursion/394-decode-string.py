def decodeString(s):
    stack = []
    for c in s:
        if c == "]":
            temp = ""
            while stack[-1] != "[":
                temp = stack.pop() + temp
            stack.pop()
            num = ""
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            num = int(num)
            stack.append(num * temp)
        else:
            stack.append(c)
    return "".join(stack)
print(decodeString("2[abc]3[cd]ef"))