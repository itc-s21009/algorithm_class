MAX = 5
stack = [0]*MAX
sp = 0

def push(d):
    global sp
    if sp < MAX:
        stack[sp] = d
        sp += 1
        print(f'データ {d} を追加しました')
    else:
        print('これ以上データを追加できません')

def pop(d):
    global sp
    if sp > 0:
        sp -= 1
        return stack[sp]
    else:
        print('取り出すデータが存在しません')
        return None

for i in range(6):
    push(i)
for i in range(6):
    d = pop(i)
    print(f'取り出したデータ: {d}')