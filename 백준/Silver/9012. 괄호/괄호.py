n = int(input())
for i in range(n):
    stack = []
    line = input()
    for i in line:
        if stack:
            if i == '(':

                stack.append(i)

            elif i == ')':
                if stack[-1] == '(':
                    stack.pop()

                else:
                    stack.append(i)

        else:
            stack.append(i)

    if stack:
        print("NO")
    else:
        print("YES")