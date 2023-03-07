n = int(input())
def fibo(n):
    if(n==1 or n ==2):
        return 1
    elif(n==0):
        return 0
    else:
        return fibo(n-1)+fibo(n-2)

print(fibo(n))