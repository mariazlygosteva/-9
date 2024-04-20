def domino_dots(n):
    total_dots = 0
    for i in range(n + 1):
        for j in range(i + 1):
            total_dots += i + j
    return total_dots

n = int(input('Введите максимальное количество точек на плитке кости домино: '))
print('Общее количество точек на всех домино:', domino_dots(n))