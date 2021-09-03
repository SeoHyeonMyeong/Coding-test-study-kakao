num_left = [1,4,7]
num_right = [3,6,9]
num_mid = [2,5,8,0]


def distance(coord1, coord2):
    x = abs(coord1[0] - coord2[0])
    y = abs(coord1[1] - coord2[1])
    return x+y

def solution(numbers, hand):
    ans = ""
    if hand == "left": 
        left_advantage = 0.5
        right_advantage = 0
    if hand == "right": 
        right_advantage = 0.5
        left_advantage = 0

    left_hand = [0,3]
    right_hand = [2,3]

    for num in numbers:
        if num in num_left:
            ans += "L"
            left_hand = [0,num_left.index(num)]
        elif num in num_right:
            ans += "R"
            right_hand = [2,num_right.index(num)]
        elif num in num_mid:
            coord = [1,num_mid.index(num)]
            left_distance = distance(coord,left_hand) - left_advantage
            right_distance = distance(coord,right_hand) - right_advantage
            if left_distance < right_distance:
                ans += "L"
                left_hand = coord
            else:
                ans += "R"
                right_hand = coord
    return ans


numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

print(solution(numbers, hand))