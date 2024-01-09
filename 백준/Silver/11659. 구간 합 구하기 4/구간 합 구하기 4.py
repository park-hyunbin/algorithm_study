import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix = [0]
temp = 0

#현재 숫자의 합

for i in numbers :
    temp = temp + i
    prefix.append(temp)

for i in range(quizNo) :
    s, e = map(int,input().split())
    print(prefix[e] - prefix[s-1])

