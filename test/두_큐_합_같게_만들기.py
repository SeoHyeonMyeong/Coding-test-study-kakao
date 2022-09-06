from collections import deque

def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    sum1 = sum(queue1)
    sum2 = sum(queue2)

    total = sum1 + sum2
    diff = sum1 - sum2
    count = 0

    # 전체 합이 홀수인 경우
    if total % 2 != 0:
        return -1

    # 탐욕법 많은쪽 queue에서 덜어서 적은쪽 queue로 전달
    for i in range(len(queue1) * 3):
        print(diff)
        if diff == 0:
            return count
        elif diff > 0:
            item = queue1.popleft()
            diff -= item * 2
            queue2.append(item)
        else:
            item = queue2.popleft()
            diff += item * 2
            queue1.append(item)
        count += 1

    # Queue 길이의 3배만큼 순회를 돌리고 답이 없으면 오답 처리
    return -1


if __name__ == '__main__':
    q1 = [1, 1, 1, 8, 10, 9]
    q2 = [1, 1, 1, 1, 1, 1]
    print("count:", solution(q1, q2))
