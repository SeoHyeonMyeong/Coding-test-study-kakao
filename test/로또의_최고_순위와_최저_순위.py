lottos = [44,1,0,0,31,25]
win_nums = [31,10,45,1,6,19]

rate = [6,6,5,4,3,2,1]

def solution(lottos, win_nums):
    wrong = 0
    right = 0
    for i in lottos:
        if i in win_nums:
            right += 1
        elif i != 0:
            wrong += 1
    return [rate[6-wrong] , rate[right]]

print(solution(lottos, win_nums))