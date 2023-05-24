LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, 10],
    [3, 4, 20],
    [5, None, 30],
    [6, 7, 40],
    [None, None, 50],
    [None, None, 60],
    [None, None, 70],
    [None, None, 80],
]
MAX = len(node)
print('指定の番号のノードを調べます')
print('何も入力せずにEnterを押すと終了します')

while True:
    s = input('number=')
    if s == '':
        break
    n = int(s)
    if 0 <= n and n < MAX:
        print(f'node{n}の値は{node[n][DATA]}')
        le = node[n][LEFT]
        if le != None:
            print(f'左の子は{node[le][DATA]}')
        else:
            print('左の子は存在しません')
        ri = node[n][RIGHT]
        if ri != None:
            print(f'右の子は{node[ri][DATA]}')
        else:
            print('右の子は存在しません')
    else:
        print(f'0から{MAX-1}の範囲で入力してください')
