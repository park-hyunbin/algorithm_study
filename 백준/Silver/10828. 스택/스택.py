import sys

n = int(input())

items = []

for _ in range(n):
    word = sys.stdin.readline().split()

    if word[0] == 'push':
        items.append(word[1])

    elif word[0] == 'pop':
        if len(items) == 0:
            print(-1)
        else:
            print(items.pop())

    elif word[0] == 'size':
        print(len(items))

    elif word[0] == 'empty':
        if len(items) == 0 :
            print(1)
        else :
            print(0)

    elif word[0] == 'top':
        if len(items) == 0 :
            print(-1)
        else :
            print(items[-1])