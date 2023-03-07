
n = int(input())
for _ in range(n):
    score_list = list(map(int,input().split()))
    avg = sum(score_list[1:])/score_list[0]

    count = 0
    rate = 0
    for i in score_list[1:]:
        if i > avg :
            count+=1

    rate = (count/score_list[0])*100
    print(f'{rate:.3f}'+'%')


