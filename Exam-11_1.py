num = int(input('数値＞ '))


def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    return 1


print(factorial(num))
