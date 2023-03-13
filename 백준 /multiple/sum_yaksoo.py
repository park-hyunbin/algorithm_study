

while True :
    list = []
    n = int(input())
    if n == -1 :
        break

    else:
        for i in range(1,n):
            if n % i == 0 :
                list.append(i)

        if n == sum(list) :
            print(str(n)+' = '+' + '.join(map(str, list)))

        else :
            print(n,"is NOT perfect.")

