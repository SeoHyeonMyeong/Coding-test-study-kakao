from collections import deque
from collections import defaultdict

def solution(n, edges):
    connection = defaultdict(list)

    for v1, v2 in edges:
        connection[v1].append(v2)
        connection[v2].append(v1)

    # distance
    def distance(start):
        
        dist = [-1] * (n+1)
        dist[start] = 0
        dist[0] = 0
        
        deq = deque([start])
        while deq:
            i = deq.popleft()
            # visit all j in node[i]
            for j in connection[i]:
                if dist[j] == -1:
                    deq.append(j)
                    dist[j] = dist[i] + 1
        return dist

    # 임의의 노드 1로부터 가장 먼 노드 A를 찾는다
    dist1 = distance(1)
    node_A = dist1.index(max(dist1))
                    
    # 노드 A로부터 각 노드까지의 거리를 찾는다.
    dist_A = distance(node_A)
    
    # 가장 먼 거리의 노드가 여러개라면 2개를 선택하여
    # f(a,b,c)를 하면 되므로 가장 먼 거리 리턴
    count_A = dist_A.count(max(dist_A))
    if count_A > 1:
        return max(dist_A)
    
    # 가장 먼 거리의 노드가 하나면 노드 B로 설정
    node_B = dist_A.index(max(dist_A))

    
    # 노드 B로부터 각 노드까지의 거리를 찾는다.
    dist_B = distance(node_B)
    
    # 가장 먼 거리의 노드가 여러개라면 2개를 선택하여
    # f(a,b,c)를 하면 되므로 가장 먼 거리 리턴
    count_B = dist_B.count(max(dist_B))
    if count_B > 1:
        return max(dist_B)
    
    # 아니라면 지름 - 1 을 반환
    return max(dist_B)-1

n = 4
edges = [[1,2],[2,3],[3,4]]	

n = 5
edges = [[1,5],[2,5],[3,5],[4,5]] 

n = 11
edges = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [6, 10], [10, 11]]

print(solution(n,edges))