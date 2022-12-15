s = '[{}{}(]'
stack = []
for i in s:
    if i == '[' or i == '{' or i == '(':
        stack.append(i)


    elif i == ']' and len(stack) > 0:
        l = stack.pop()
        if l != '[':
            print('Not Balanced')
            break

    elif i == ')' and len(stack) > 0:
        l = stack.pop()
        if l != '(':
            print('Not Balanced')
            break

    elif i == '}' and len(stack) > 0:
        l = stack.pop()
        if l != '{':
            print('Not Balanced')
            break
    else:
        print('not balanced')
        break
else:
    print('balanced')
