import random
n = 0
r = random.randint(1, 100)
print('１から１００の数を当てるゲームです')
while True:
    n += 1
    a = int(input('数を入力してください: '))
    if r == a:
        print(f'{n}回で正解です')
        break
    if r > a:
        print('それより大きい数です')
    else:
        print('それより小さい数です')