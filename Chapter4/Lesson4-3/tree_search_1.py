LEFT = 0
RIGHT = 1
DATA = 2
node = [
    [1, 2, 10],
    [3, 4, 5],
    [5, None, 12],
    [None, None, 2],
    [6, 7, 8],
    [None, None, 11],
    [None, None, 6],
    [None, None, 9],
]

def traverse(p, level=1):
    if p != None:
        print(f'{node[p][DATA]}のひだり を見ます')
        traverse(node[p][LEFT], level+1)
        print(f'Lv{level}: {node[p][DATA]}')
        print(f'{node[p][DATA]}のみぎを見ます')
        traverse(node[p][RIGHT], level+1)

print('二分探索木を通りがけ順に巡回')
traverse(0)
