import numpy as np

def rotate_90(m):
    N = len(m)
    ret = [[0] * N for _ in range(N)]
    for r in range(N):
    	for c in range(N):
            ret[c][N-1-r] = m[r][c]
    return np.array(ret)


def solution(key, lock):
    # lock 반전
    new_lock = []
    for line in lock:
        line = map(lambda x: 1 if (x==0) else 0,line)
        new_lock.append(list(line))
    lock = new_lock

    N = len(lock)
    M = len(key)
    K = M + N + N - 2

    # 키의 상하좌우에 N-1 만큼 padding 추가
    new_key = np.zeros((K,K))
    new_key[N-1:K-N+1,N-1:K-N+1] = np.array(key)

    lock = np.array(lock)
    key = new_key

    # lock 을 90도로 돌린 4개를 lock_arr 배열로 선언
    lock_arr = []
    while len(lock_arr) < 4:
        lock_arr.append(lock)
        lock = rotate_90(lock)
    
    # lock과 상응하는 구역의 sub_key가 lock_arr에 있는지 찾아냄  
    for i in range(K-N+1):
        for j in range(K-N+1):
            sub_key = key[i:i+N, j:j+N]
            for lock in lock_arr:
                if np.array_equal(lock,sub_key):
                    return True
    # 없을 경우 false
    return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 0, 1], [1, 1, 0], [1, 1, 1]]
print(solution(key,lock))