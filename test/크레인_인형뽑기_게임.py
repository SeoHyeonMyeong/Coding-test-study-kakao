def solution(board, moves):
    board = list(map(list,zip(*board)))
    stack = [-1]
    num_delete = 0
    for line in board:
        while line[0] == 0:
            line.remove(0)
    for i in moves:
        if len(board[i-1]) == 0:
            pass
        else:
            pick = board[i-1].pop(0)
            if pick == stack[-1]:
                stack.pop()
                num_delete +=2
            else:
                stack.append(pick)
    return num_delete

# board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
# moves = [1,5,3,5,1,2,1,4]
# print(solution(board,moves))