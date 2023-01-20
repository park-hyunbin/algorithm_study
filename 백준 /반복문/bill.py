money = 0 
x = int(input())
n = int(input())
    
for i in range(1,n+1):
    a, b = map(int,input().split())
    money += a*b

if(money == x):
    print("Yes")
else : 
    print("No")