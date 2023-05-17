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

def main():
    for i in range(2):
        push(i)
    for i in range(1):
        d = pop(i)
        print(f'取り出したデータ: {d}')
    for i in range(3):
        push(i)

if __name__ == '__main__':
    main()