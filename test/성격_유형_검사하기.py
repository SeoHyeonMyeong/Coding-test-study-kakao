from collections import defaultdict


def solution(survey, choices):
    score = defaultdict(int)
    indices = ["RT", "CF", "JM", "AN"]
    answer = ""

    # 각 항목의 점수를 계산
    for s, c in zip(survey, choices):
        a, b = s[0], s[1]
        score[a] += max(4 - c, 0)
        score[b] += max(c - 4, 0)

    # 지표별 유형 판별
    for index in indices:
        a, b = index[0], index[1]
        if score[a] >= score[b]:
            answer += a
        else:
            answer += b
    return answer



if __name__ == "__main__":
    s = ["AN", "CF", "MJ", "RT", "NA"]
    c = [5, 3, 2, 7, 5]
    print(solution(s, c))
