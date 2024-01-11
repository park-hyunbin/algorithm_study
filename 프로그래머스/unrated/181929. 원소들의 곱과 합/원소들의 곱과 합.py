def solution(num_list):
    product = 1
    total_sum = 0
    
    for num in num_list:
        product *= num
        total_sum += num
    
    if product < total_sum ** 2:
        answer = 1
    else:
        answer = 0
    
    return answer
