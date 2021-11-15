from collections import deque
def solution(n, edge):
    
    tmp = [1]
    new_tmp = []
    graph = [[] for i in range(0, n+1)]
    visited = [False for i in range(0, n+1)]
    visited[1] = True

    for i in edge:
        a,b = i
        graph[a].append(b)
        graph[b].append(a)

    while True:
        for a in tmp:
            for b in graph[a]:
                if not visited[b]:
                    visited[b] = True
                    new_tmp.append(b)

        if new_tmp != []:
            tmp = new_tmp
            new_tmp = []
        else:
            break

    if len(new_tmp)==0:
        return len(tmp)
    return len(new_tmp)

# n = 6
# vertex = [[1,6], [4,3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
# print(solution(n,vertex))