def solution(n):
    if n % 2 == 1: 
        sum_odd = 0
        for i in range(1, n+1,2):
            sum_odd += i
        return sum_odd
    else: 
        sum_even = 0 
        for i in range(2, n+1, 2): 
            sum_even += i * i
        return sum_even
    
    answer = solution(n)
    return answer
