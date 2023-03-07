import sys
n = int(sys.stdin.readline())
check = n
count = 0

while True :
    sum = n//10 + n%10
    new = n%10*10 + sum%10
    count += 1

    n = new

    if new == check :
        break

print(count)