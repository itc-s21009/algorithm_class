MAX = 6
que = [0]*MAX
head = 0
tail = 0

def enqueue(d):
    global tail
    nt = (tail+1)%MAX

    if nt == head:
        print('これ以上データを入れられません')
    else:
        que[tail] = d
        tail = nt
        print(f'データ {d} を追加しました')

def dequeue():
    global head
    if head == tail:
        print('取り出すデータが存在しません')
        return None
    else:
        d = que[head]
        que[head] = 0
        head = (head + 1)%MAX
        print(f'{d} を取り出しました')
        return d

for i in range(6):
    enqueue(i)

for i in range(6):
    dequeue()
