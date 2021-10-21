from collections import deque

def solution(number, k):
    ans = deque()
    number = deque(number)
    count = 0
    while count < k:
        # 다했는데도 횟수가 남으면 뒤에서 삭제
        if len(number) == 0:
            for i in range(k-count):
               ans.pop() 
            break

        # 왼쪽이 비어있으면 왼쪽에 추가
        if len(ans) == 0:
            ans.append(number.popleft())
        
        
        else:
            left = ans.pop()
            right = number.popleft()
            # 우측이 크면 왼쪽 삭제
            if left < right:
                number.appendleft(right)
                count += 1
            # 우측이 작으면 왼쪽으로 이동
            else:
                ans.append(left)
                ans.append(right)
    

    return "".join(ans+number)

number = "99999"
k = 4
print(solution(number,k))