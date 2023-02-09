# n = int(input('Введите число: '))
# factorial = 1
# while n > 1:
#     factorial *= n
#     n -= 1
# print(factorial)

def factorial(n):
    proizvedenie = 1
    for i in range(2, n+1):
        proizvedenie = proizvedenie * i
        print(proizvedenie)


factorial(5)
