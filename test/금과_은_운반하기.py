from collections import deque

from numpy import flexible

def solution(a, b, g, s, w, t):

    # 도시 정리
    cities = []
    for i in range(len(t)):
        cities.append([g[i],s[i],w[i],t[i]])

    # binary search
    time_1 = 1
    time_2 = 1e9 * 2 * 1e5 * 2
    while True:
        time_mid = int((time_1 + time_2) / 2)
        temp_a = 0
        temp_b = 0
        temp_flex = 0

        for city in cities:
            g, s, w, t = city
            if time_mid < t:
                pass
            else:
                chance = int((time_mid - t) / (2 * t)) + 1
                weight_sum = chance * w

                if g + s <= weight_sum:
                    temp_a += g
                    temp_b += s
                elif g < weight_sum and s < weight_sum:
                    flex = g + s - weight_sum
                    temp_a += g - flex
                    temp_b += s - flex
                    temp_flex += flex
                elif g <= weight_sum and s >= weight_sum:
                    temp_flex += g
                    temp_b += weight_sum - g
                elif g >= weight_sum and s <= weight_sum:
                    temp_flex += s
                    temp_a += weight_sum - s
                else:
                    temp_flex += weight_sum

        diff_a = a - temp_a
        diff_b = b - temp_b
        if diff_a > 0:
            temp_flex -= diff_a
        if diff_b > 0:
            temp_flex -= diff_b

        if temp_flex < 0:
            if time_mid == time_1:
                return time_2
            time_1 = time_mid
        else:
            time_2 = time_mid
            if time_2 -1 == time_1:
                return time_2

# a = 10
# b = 10
# g = [1e9]
# s = [1e9]
# w = [100]
# t = [10000]

a = 90
b = 500
g = [70, 70, 0]
s = [0, 50, 500]
w = [100, 100, 2]
t = [4, 8, 1]

print(solution(a,b,g,s,w,t))

