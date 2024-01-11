def solution(num_list):
    odd_numbers = []
    even_numbers = []
    
    for i in num_list:
        if i % 2 != 0:
            odd_numbers.append(i)
        else:
            even_numbers.append(i)
    
    odd_str = int(''.join(map(str, odd_numbers)))
    even_str = int(''.join(map(str, even_numbers)))
    
    return odd_str+even_str
