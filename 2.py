num = float(input('Введите положительное число, большее 2: '))
if num <= 2:
    print('Число должно быть больше 2.')
else:
    while num > 2:
        print('%.3f' % num)
        num = num ** 0.5
    print('%.3f' % num)