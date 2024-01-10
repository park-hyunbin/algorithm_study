def solution(a, b):
    a = str(a)
    b = str(b)
    
    A = a+b
    B = b+a
    
    A = int(A)
    B = int(B)

    if A > B : 
        answer = A 
    else : 
        answer = B 
    return answer