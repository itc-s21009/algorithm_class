def euclid(a, b):
    if b == 0:
        print(f'return {a}')
        return a
    else:
        print(f'{a}%{b} = {a%b}')
        return euclid(b, a%b)

print('a>=b>=cとなる自然数を入力してください')
a = int(input('a='))
b = int(input('b='))
c = int(input('c='))
d = euclid(a, b)
print('それらの数の最大公約数は', euclid(c, d))