# autor: robot Verter
print("Задача №1:")


def fibo(x, y):
    current, next = 1, 1
    num = []

    for _ in range(y + 1):
        num.append(current)
        current, next = next, current + next

    return num[x:y]


print(fibo(10, 20))
print('-' * 50)

print("Задача №2:")


def sort_to_max(origin_list):
    sort = list.copy(origin_list)
    sort_len = len(sort)

    for _ in range(sort_len):
        for q in range(sort_len - 1):
            if sort[q] > sort[q + 1]:
                sort[q], sort[q + 1] = sort[q + 1], sort[q]

    return sort


sort_to_max([2, 10, 4, 7, -12, -4, -9, 3, 8, 13, 9, 5])

print(sort_to_max([2, 10, 7, 4, -12, -4, -9, 8, 3, 13, 9, 5]))
print('-' * 50)

print("Задача №3:")


def filter(func, collect):
    new = []

    for x in collect:
        if func(x):
            new.append(x)

    return new


list_src = [1, 2, 3, 4, 5]

print(
    filter(
        lambda w: w % 2 == 0, list_src
    )
)
print('-' * 50)

print("Задача №4:")

def check_point(a1, a2, a3, a4):
    x1 = (a1['x'] + a3['x']) / 2
    x2 = (a2['x'] + a4['x']) / 2
    y1 = (a2['y'] + a3['y']) / 2
    y2 = (a2['y'] + a4['y']) / 2

    if x1 == x2 and y1 == y2:
        return True
    else:
        return False
