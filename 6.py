def multiply_two_digit_numbers(A, B):
  C = (A // 10) * (B // 10)
  A = A % 10
  B = B % 10
  A = A * 10 + C
  B = B * 10 + (A // 10)
  C = A % 10
  result = C * 100 + A * 10 + B
  return result

A = int(input('Введите первое число: '))
B = int(input('Введите второе число: '))

# Выводим результат
print('Произведение:', multiply_two_digit_numbers(A, B))