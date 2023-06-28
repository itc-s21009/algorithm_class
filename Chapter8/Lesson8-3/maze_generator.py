maze_str = []
wall = 'W'
way = 'O'
print(f'壁を{wall}, 通路を{way}として迷路を入力してください(空白で終了):')
s = input()
while s != '':
    maze_str.append(s)
    s = input()

def assort(c):
    if c == 'W':
        return 99
    elif c == 'O':
        return 0

print('[')
for line in maze_str:
    l = list(map(assort, line))
    print(f'\t{l}')
print(']')