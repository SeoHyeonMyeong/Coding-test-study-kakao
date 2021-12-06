from collections import deque

count = dict()
# 슬라이딩 윈도우
def solution(gems):
    # 보석 셋
    gem_set = set(gems)
    # 보석 갯수 세기
    for gem in gem_set:
        count[gem] = 0

    window = deque()
    gems = deque(gems)

    window_start = 1
    window_end = 1
    length = 1000000
    ans = []

    # 슬라이딩 윈도우 시작
    while True:
        window_leng = window_end - window_start
        # 윈도우 길이가 실제 길이와 같아지면 앞을 제거하며 전진
        if window_leng == length:
            if len(gems) == 0: break
            gem = window.popleft()
            count[gem] -= 1
            window_start += 1

            gem = gems.popleft()
            count[gem] += 1
            window_end += 1
            window.append(gem)

        # 초반에 최소길이를 찾기 전까지는 뒤를 확장하며 전진
        else:
            gem = gems.popleft()
            count[gem] += 1
            window_end += 1
            window.append(gem)
        
        # 조건을 만족하면
        if (not 0 in count.values()):
            # 초반 최소 길이를 찾은 경우
            window_leng = window_end - window_start
            if length > window_leng:
                length = window_end - window_start
                ans = [window_start, window_end - 1]
            
            # 길이 축소가 가능한 경우 앞을 제거
            while True:
                gem = window.popleft()
                if count[gem] == 1:
                    window.appendleft(gem)
                    break 
                else:
                    count[gem] -= 1
                    length -= 1
                    window_start += 1
                    ans = [window_start, window_end - 1]
    return ans



# g = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]     # 3,7
# g = ["AA", "AB", "AC", "AA", "AC"]      # 1,3
# g = ["XYZ", "XYZ", "XYZ"]       #  1,1
# g = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]        # 1,5
# g = ["A","A","A","B","B"]   # 3,4
# g = ["A"]       # 1,1
g = ["A","B","B","B","B","B","B","C","B","A"]       # 8,10

print(solution(g))