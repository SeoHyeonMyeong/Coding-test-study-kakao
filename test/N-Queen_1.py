import numpy as np
n = 8
max_queen = 4

arr = np.zeros((n,n))
global ans
ans = 0

def factorial(num):
    if num ==1:
        return 1
    else:
        return factorial(num-1) * num

def row_attack(arr, x, y):
    for j in range(n):
        if j != y:
            if arr[x,j] == 2:
                return arr, 1
            else:
                arr[x,j] = 1
    return arr, 0

def column_attack(arr, x, y):
    for i in range(n):
        if i !=x:
            if arr[i,y] == 2:
                return arr, 1
            else:
                arr[i,y] = 1
    return arr, 0

def diagonal_attack(arr, x, y):
    for j in range(n):
        for i in range(n):
            if x != i and y != j and abs(x-i) == abs(y-j):
                if arr[i,j] == 2:
                    return arr, 1
                else:
                    arr[i,j] = 1
    return arr, 0

def attack(arr, x, y):
    arr, collide_1 = row_attack(arr,x,y)
    arr, collide_2 = column_attack(arr,x,y)
    arr, collide_3 = diagonal_attack(arr,x,y)
    collide = collide_1 + collide_2 + collide_3
    return arr, collide

def find_none(arr):
    indices = np.where(arr == 0)
    indices = np.transpose(indices)
    return indices

def drop_queen(arr, index, count):
    global ans
    x = index[0]
    y = index[1]
    arr[x,y] = 2
    count = count + 1
    if count == max_queen:
        print(arr)
        ans = ans + 1
        return
    else:
        arr, collide = attack(arr, x, y)
        if(collide):
            return
        else:
            index_ = find_none(arr)
            if index_.size ==0:
                return
            for i in index_:
                drop_queen(arr.copy(),i,count)

index = find_none(arr)
for i in index:
    count = 0
    drop_queen(arr.copy(),i,count)
ans = ans / factorial(n)
ans = int(ans)
print(ans)