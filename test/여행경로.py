def solution(tickets):
    # 그래프 선언
    graph = dict()
    for ticket in tickets:
        a,b = ticket
        if not a in graph:
            graph[a]=[b]
        else:
            graph[a].append(b)
    
    for key in graph:
        graph[key].sort()
    # 여행 시작
    def dfs(a, path):
        # 길이 충족시 통과
        if len(path) == len(tickets) + 1:
            return path
        # 그래프에 없을시 패스
        if not a in graph:
            return False
        # 그래프에 선택사항이 많을 경우 재귀함수
        for i, b in enumerate(graph[a]):
            # 그래프에 해당 도시를 없애고
            graph[a].pop(i)
            new_path = path.copy()
            new_path.append(b)
            # 깊이 탐색
            result = dfs(b,new_path)

            # 하위 결과를 받아옴
            if result:
                return result

            # 그러고도 False이면 해당 도시를 되돌리고 다음 선택지 반복
            graph[a].insert(i,b)
    ans = dfs("ICN",["ICN"])
    return ans

# t = [["ICN", "AOO"], ["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]]
# print(solution(t))