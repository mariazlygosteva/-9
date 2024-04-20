import math


def ways(x):
    count = 0
    for a in range(1, int(math.sqrt(x)) + 1):
        b = math.sqrt(x - a * a)
        if b.is_integer() and b >= a:
            count += 1
    return count

x = int(input('Введите натуральное число x: '))
print(f'Количество способов представить в виде суммы квадратов двух натуральных чисел: {ways(x)}')