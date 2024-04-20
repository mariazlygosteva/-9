R, d, N = map(int, input('Введите через пробел N, d, R: ').split())
L = 0
L += 2*d*N + R*2*N + 11*(N-1)
print('Длина цепочки в мм:', L)