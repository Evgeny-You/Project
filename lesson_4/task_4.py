a = input('Введеная строка: ')

f = a[0::2]
d = a[1::2]
a.strip()
print(f)
print(d)

print(a.strip(), end='\n\n')
print(f,d, sep='     ', end='!!!')