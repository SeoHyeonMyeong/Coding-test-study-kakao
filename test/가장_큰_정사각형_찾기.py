def check_square(arr,n):
    count = 0
    for i in arr:
        if i < n:
            count = 0
        else:
            count += 1
        if count == n:
            return True
    return False

def solution(board):
    n_row = len(board[0])
    last_row = [0] * n_row
    x = 0
    for row in board:
        for i in range(n_row):
            if row[i] == 0:
                last_row[i] = 0
            else:
                last_row[i] += 1
        if check_square(last_row,x+1):
            x += 1
    return x ** 2

print(solution([[0,0,1,1],[1,1,1,1]]))
