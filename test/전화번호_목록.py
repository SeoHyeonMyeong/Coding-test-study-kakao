def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

phone_book = ["119", "97674223", "1195524421"]
print(solution(phone_book))


def solution_2(phone_book):
    for i in range(len(phone_book)):
        pivot = phone_book[i]
        for j in range(i+1, len(phone_book)):
            strlen = min(len(pivot), len(phone_book[j]))
            if pivot[:strlen] == phone_book[j][:strlen]:
                return False
        return True