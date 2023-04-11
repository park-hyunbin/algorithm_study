n = int(input())

for i in range (n) :
    num = int(input())
    q = num // 25
    d = (num%25) //10
    ni = ((num%25)%10) // 5
    p = ((num%25)%10) % 5
    print(q,d,ni,p)