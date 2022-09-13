from collections import deque

# 문제 1 : 거스름돈
# 500원, 100원, 50원, 10원이 있을때 돈을 거슬러 줄 수 있는 최소 동전의 수
# 탐욕법으로 500원 -> 100원 -> 50원 -> 10원 순서로 동전을 고르면 됩니다.
# 큰 단위가 항상 작은 단위의 배수이므로 작은 단위의 동전들을 종합해 다른 해가 나올 수 없기 때문입니다.

money = 3700

coin = [500, 100, 50, 10]
count = 0
for c in coin:
    count += money // c
    money %= c
print(count)

# 문제 2 : 1이 될때까지
# 어떠한 수 N이 1이 될때까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다.
# 단, 두번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있습니다.
# 1. N에서 1을 뺍니다.
# 2. N을 K로 나눕니다.
# 나눌 수 있으면 무조건 나누는게 빠르게 수를 줄일 수 있다.

N = 17
K = 4

count = 0
while N != 1:
    count += 1
    if N % K == 0:
        N = N // K
    else:
        N -= 1
print(count)


# 문제 3 : 곱하기 혹은 더하기
# 각자리가 숫자로만 이루어진 문자열 S에서 하나씩 숫자를 확인하여 x, + 연산자를 넣어
# 결과적으로 만들어 질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요, 모든 연산은 왼쪽에서 부터 순서대로 이루어 집니다.
S = '567'
ans = 0

for i in S:
    if int(i) <= 1 or ans <= 1:
        ans += int(i)
    else:
        ans *= int(i)
print(ans)


# 문제 4 : 모험가 길드
# '공포도'가 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여해야 합니다.
# N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 최대 그룹수는?

people = [2, 3, 1, 2, 2]

people = deque(sorted(people))
i = 0
count = 0
while people:
    p = people.popleft()
    i += 1
    if i >= p:
        count += 1
        i = 0
print(count)

