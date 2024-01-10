def solution(a, b):
    B = 2*a*b
    
    a = str(a)
    b = str(b)
    
    A = a+b 
    A = int(A)
    
    answer = max(A,B)
    return answer