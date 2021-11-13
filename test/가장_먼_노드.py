from collections import deque
def solution(n, edge):
    lst = list(range(1,n+1))
    tmp = [1]
    new_tmp = []
    edge = deque(edge)
    count = 0
    n = len(edge)
    while len(edge) > 0:
        if count >= n:
            tmp = new_tmp
            new_tmp = []
            count = 0
            n = len(edge)
        count += 1
        v = edge.popleft()
        print(tmp, new_tmp)
        a = v[0]
        b = v[1]
        if a in tmp:
            if not b in tmp and not b in new_tmp:
                new_tmp.append(b)
        elif b in tmp:
            if not a in tmp and not a in new_tmp:
                new_tmp.append(a)
        else:
            edge.append(v)
    return len(new_tmp)

n = 6
vertex = [[3,6], [4,3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n,vertex))