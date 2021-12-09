def solution(n, wires):
    # 연결, 연결수, 노드의 값
    connection = dict()
    count = dict()
    value = dict()

    for i in range(1,n+1):
        count[i] = 0
        value[i] = 1
        connection[i] = []
    
    for a,b in wires:
        connection[a].append(b)
        connection[b].append(a)
        count[a] +=1
        count[b] +=1
    
    # 말단일 경우 병합 대상
    tmp = []
    for i in range(1,n+1):
        if count[i] == 1:
            tmp.append([i,value[i]])

    # 무한 반복
    while tmp:
        # 말단 노드중 값이 제일 작은 경우 합치기 진행
        tmp.sort(key=lambda x: x[1] + value[connection[x[0]][0]],reverse=True)
        print(tmp, count)
        # 병합되는 노드 i 병합하는 노드 j
        i,val = tmp.pop()
        j = connection[i][0]
        count[j] -= 1
        value[j] += val

        connection[j].remove(i)
        count[i] = 0
        value[i] = 0

        if count[j] == 1:
            tmp.append([j,value[j]])
            
        # 종료 조건
        if sum(count.values()) == 2:
            b = abs((n/2) - value[j])
            return int(b * 2)



n = 7
wires = [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]

n = 10
wires = [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9],[4,10]]

print(solution(n,wires))
