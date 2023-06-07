LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, "38.5℃以上の発熱がある？"],
    [3, 4, "元気がある？"],
    [5, 6, "むねがひいひい？"],
    [None, None, "氷枕で病院"],
    [None, None, "様子をみる"],
    [None, None, "解熱剤で病院"],
    [None, None, "速攻で病院"],
]

i = 0
while node[i][LEFT] and node[i][RIGHT]:
    s = input(f'{node[i][DATA]}(Y/n): ').lower()
    if s == 'y':
        i = node[i][RIGHT]
    elif s == 'n':
        i = node[i][LEFT]
print(f'診断結果: {node[i][DATA]}')