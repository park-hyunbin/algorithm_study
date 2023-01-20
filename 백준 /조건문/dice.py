A, B, C = map(int,input().split())
if(A==B==C):
    print(10000+A*1000)
elif(A==B or B==C or A==C):
    if(A==B):
        print(1000+100*A)
    elif(B==C):
        print(1000+100*B)
    elif(A==C):
        print(1000+100*A)
else : 
    if(A-B>0 and A- C>0):
        print(A*100)
    elif(B-A>0 and B- C>0):
        print(B*100)
    elif(C- A>0 and C- B>0): 
        print(C*100)

