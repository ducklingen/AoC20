def sum(a, b):
    print(str(a+b))

sum(*[1, 2])

print(str(123 & 456))

dict = {'a': 1, 'b': 2}

if 'c' in dict.keys():
    print('Nop')
else:
    print('Jep')