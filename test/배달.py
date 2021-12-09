def solution(N, road, K):
    distance = dict()
    connection = dict()
    shortest_distance = dict()

    for i in range(1,N+1):
        connection[i] = []
        shortest_distance[i] = 500001
    shortest_distance[1] = 0

    for a,b,dist in road:
        # 연결, 거리 기록
        key = str(a) + "," + str(b)
        if a > b:
            key = str(b) + "," + str(a)
        if key in distance:
            distance[key] = min(distance[key],dist)
        else:
            distance[key] = dist
            connection[a].append(b)
            connection[b].append(a)

    # 마을, 남은 시간
    tmp = [[1,K]]
    ans = [1]
    while tmp:
        # a 시작마을, b 도착마을, time 남은시간
        a,time = tmp.pop()
        lst = connection[a]
        for b in lst:
            key = str(a) + "," + str(b)
            if a > b:
                key = str(b) + "," + str(a)
            dist = distance[key]
            
            # 도달 가능하면
            if dist <= time:
                last = time - dist
                if K-last <= shortest_distance[b]:
                    shortest_distance[b] = K-last
                    tmp.append([b,last])
                if not b in ans:
                    ans.append(b)
    return len(ans)