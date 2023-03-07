n = int(input())

for _ in range(n):
    kh = ""
    R, S = input().split()
    for i in S:
        kh += i*int(R)
    print(kh)










