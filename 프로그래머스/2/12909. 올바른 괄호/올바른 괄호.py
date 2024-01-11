def solution(s):
    list = []
    for i in s : 
        if i == '(' : 
            list.append(i)
        elif len(list) >= 1 and i == ')' :
            list.pop()
        else : return False 

    return False if len(list) >=1 else True