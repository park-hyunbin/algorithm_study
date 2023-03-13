n = int(input())
for _ in range(n):
    m = int(input())

    prime = []
    def is_prime(x):
        for i in range(2,x):
            if x%i==0:
                break
        else :
            prime.append(x)

    for i in prime :
        m = prime[i]+ prime[i]
        print(prime[i], prime[i])






