def palindrome(number):
    return str(number) == str(number)[::-1]

def mileage():
    for i in range(100000, 1000000):
        if palindrome(i + 3):
            if palindrome((i + 2) // 10 % 10000):
                if palindrome((i + 1) % 100000) and palindrome(i % 100000):
                    print('Пробег в момент первого замечания: ', i)
                    break
mileage()