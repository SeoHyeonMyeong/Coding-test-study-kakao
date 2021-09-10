def solution(triangle):
    last = [0]
    for row in triangle:
        for i in range(len(row)):
            if i == 0:
                row[i] += last[i]
            elif i == len(row)-1:
                row[i] += last[i-1]
            else:
                row[i] += max(last[i],last[i-1])
        last = row.copy()
    return max(last)

tri = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(tri))