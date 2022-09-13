from collections import Counter

# 구현
# 알고리즘은 간단하지만 코드가 지나치게 길어지는 문제
# 실수 연산을 다루고, 특정 소수점 자리까지 출력해야 하는 문제
# 문자열을 특정한 기준에 따라서 끊어 처리해야 하는 문제
# 적절한 라이브러리르 찾아서 사용해야 하는 문제


# 문제 1: 상하좌우
# N x N 크기의 정사각형 공간에서 가장 왼쪽 위 좌표는 (1, 1), 가장 오른쪽 아래 좌표는 (N, N) 입니다.
# 여행가는 (1, 1) 에서 출발합니다. L, R, U, D의 계획서 배열이 주어집니다. 최종좌표의 (x,y)를 구하세요

n = 5
A = "RRRLUDD"

c = Counter(A)

hor = c['R'] - c['L'] + 1
ver = c['U'] - c['R'] + 1

while True:
    if hor < 1:
        hor += n
        continue
    if hor > n:
        hor -= n
        continue
    if ver < 1:
        ver += n
        continue
    if ver > n:
        ver -= n
        continue
    break
print(hor, ver)

# 문제 2: 시각
# 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수 구하기
N = 5

N += 1
count_h = 3600
count_3_in_60 = sum([1 for i in range(1, 60) if '3' in str(i)])
count_not3_in_60 = 60 - count_3_in_60

count_3_in_hour = count_h - (count_not3_in_60 * count_not3_in_60)

count_3_in_N = sum([1 for i in range(1, N) if '3' in str(i)])
count_not3_in_N = N - count_3_in_N

print(count_3_in_N)
ans = (count_3_in_N * count_h) + (count_not3_in_N * count_3_in_hour)
print(ans)


# 문제3: 왕실의 나이트
# 행복 왕국의 왕실 정원은 8 x 8 좌표 평면입니다. 나이트는 L자 형태로만 이동할 수 있습니다.
# 1. 수평으로 두칸 이동한 뒤 수직으로 한 칸 이동
# 2. 수직으로 두칸 이동한 뒤 수평으로 한 칸 이동
# 체스판처럼 a1과 같은 형태로 위치가 주어 집니다.
# 첫째 줄에 나이트가 이동할 수 있는 경우의 수를 출력하세요.


# 문제4: 문자열 재정렬
# 알파벳 대문자와 숫자로만 구성된 문자열이 주어집니다. 오름차순으로 정렬하여 이어서 출력하고
# 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# ex) K1KA5cB7 -> ABCKK13
