import sys
n = int(input())
data = [int(sys.stdin.readline()) for i in range(n)]

print(round(sum(data)/n))
print(sorted(data)[len(data)//2])

