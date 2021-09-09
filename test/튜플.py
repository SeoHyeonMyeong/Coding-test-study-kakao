import numpy as np

def solution(s):
    # 앞뒤 {} 제거
    s = s[1:-1]
    # 각각의 리스트 구분
    s = s.split("},{")
    # 앞뒤 {} 제거
    s[0] = s[0][1:]
    s[-1] = s[-1][:-1]
    
    # 리스트로 변환시켜 저장
    temp = []
    for li in s:
        li = li.split(",")
        li = [int(i) for i in li]
        temp.append(li)
    
    # 길이 순서로 정렬
    temp.sort(key=lambda x:len(x))
    
    # 튜플 생성
    ans = []
    for li in temp:
        for item in li:
            if not item in ans:
                ans.append(item)
    return ans

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))