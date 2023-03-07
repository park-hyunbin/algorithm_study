n = int(input())

for _ in range(1, n+1):
    sum = 0 
    count = 0 

    list_n = list(input())
    for i in list_n:
        if i == "O":
            count += 1 
            sum += count  
        else : 
            count = 0 
        
    print(sum)

