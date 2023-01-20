H, M = map(int,input().split())
if(M>=45):
    print(H, end =' ')
    print(M-45)
else : 
    if(H==0):
        print(23, end=' ')
        print(60-(45-M))
    else:
        print(H-1, end =' ')
        print(60-(45-M))
