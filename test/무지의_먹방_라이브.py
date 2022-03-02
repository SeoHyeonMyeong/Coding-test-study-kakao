from itertools import accumulate

def solution(food_times, k):
    N = len(food_times)
    food = [False] * N

    # k가 N보다 작다면 결론 도출
    if k < N: return k + 1
    
    # 누적 합계를 순서대로 정렬
    food = sorted(food_times)
    food_acc = list(accumulate(food))
    
    # 몇번째 회전 루프에 k가 속하는지 판단하기
    limit_food = -1
    for i in range(N):
        limit = food_acc[i] + (N-(i+1)) * food[i]
        if limit > k:
            limit_food = food[i]
            # k에서 이전 회차 루프 횟수 빼기
            k -= food_acc[i-1] + (N-i) * food[i-1]
            break

    # 답이 없다면 -1 반환
    if limit_food == -1:
        return -1

    # 남은 음식
    remain_food = [idx for idx, food in enumerate(food_times) if food >= limit_food]
    return remain_food[k % len(remain_food)] + 1

food_times = [3, 1, 2]
k = 5

food_times = [4,2,3,6,7,1,5,8] # 3
k = 16

# food_times = [4,2,3,6,7,1,5,8] # 5
# k = 27

print(solution(food_times, k))



# 음식 시간 순  1 2 3 4 5 6 7 8
# 시간 누적     1 3 6 10 15 21 28 36
# 만약 2번째 줄에서 끝난다고 가정하면
# 누적[2] = 3 
# (N - 2) * 2 개수만큼 
