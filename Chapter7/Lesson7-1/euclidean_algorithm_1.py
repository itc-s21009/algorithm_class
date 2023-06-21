print('a>=bとなる自然数を入力してください')
a = int(input('a='))
b = int(input('b='))
if a < b:
    a, b = b, a
    print('aよりbのほうが大きいため、入れ替えます')
    print(f'a={a}')
    print(f'b={b}')

while True:
    r = a % b
    print(f'{a}%{b} = {r}')
    if r == 0:
        print(f'それらの数の最大公約数は{b}')
        break
    a = b
    b = r
